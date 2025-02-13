{ pkgs, lib, inputs, ... }:
let
  sink = ./sink;
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
in
{
    process.manager.implementation = "process-compose";

    services.opentelemetry-collector.enable = true;
    services.opentelemetry-collector.package = nixpkgs-unstable.opentelemetry-collector-contrib;

    services.opentelemetry-collector.configFile = ./config.yaml;

    processes.sink = {
        exec = "${pkgs.uv}/bin/uv run -p 3.13 --no-project --with-editable ${sink} obe-sink";
        process-compose = {
            readiness_probe = {
                http_get = {
                host = "localhost";
                scheme = "http";
                path = "/telemetry";
                port = 8080;
            };
            initial_delay_seconds = 1;
            period_seconds = 1;
            timeout_seconds = 5;
            success_threshold = 1;
            failure_threshold = 3;
            };
          availability.restart = "never";
      };
    };

    processes.opentelemetry-collector.process-compose = {
        depends_on.sink.condition = "process_healthy";
    };

    enterTest = lib.mkBefore ''
        # Wait for the port to be open until the timeout is reached
        wait_for_port() {
          local port=$1
          local timeout=''${2:-15}

          timeout $timeout bash -c "until ${pkgs.libressl.nc}/bin/nc -z localhost $port 2>/dev/null; do sleep 0.5; done"
        }

        export -f wait_for_port

        if [ -f ./.test.sh ]; then
          echo "• Running .test.sh..."
          ./.test.sh
        fi

        wait_for_port 8080
        wait_for_port 4319
        wait_for_port 4317
        wait_for_port 4318
    '';

}

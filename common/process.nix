{ pkgs, ... }:
let
  sink = ./sink;
in
{
    packages = [pkgs.uv];
    services.opentelemetry-collector.enable = true;
    services.opentelemetry-collector.configFile = ./config.yaml;

    process.manager.implementation = "process-compose";
    processes.sink = {
        exec = "${pkgs.uv}/bin/uv run --no-project --with-editable ${sink} obe-sink";
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
}

{ pkgs, inputs, config, ... }:

{
  packages = with pkgs; [
    (python313.withPackages (ps: with ps; [uv]))
    curl
  ];

  processes.sink = {
        exec = "${pkgs.uv}/bin/uv run --with-editable ./. obe-sink";
        process-compose = {
            readiness_probe = {
                http_get = {
                host = "localhost";
                scheme = "http";
                path = "/telemetry";
                port = 8080;
            };
            initial_delay_seconds = 1;
            period_seconds = 10;
            timeout_seconds = 5;
            success_threshold = 1;
            failure_threshold = 3;
            };
          availability.restart = "on_failure";
      };
  };

  enterTest = ''
    wait_for_port 8080
    wait_for_port 4319
    ${pkgs.curl}/bin/curl --fail http://localhost:8080/telemetry
  '';
}

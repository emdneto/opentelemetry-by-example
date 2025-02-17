{pkgs, ...}:
{
    # processes.snippet.exec = "opentelemetry-instrument flask --app snippet.py run -p 5001";
    # processes.snippet.process-compose.environment = [  "OTEL_SERVICE_NAME=flask-zero-code" ];

    enterShell = ''
        echo "entering shell devenv"
        # uv pip install -r requirements.txt
        # opentelemetry-bootstrap -a install
    '';

    enterTest = ''
        wait_for_port 8080
        ${pkgs.curl}/bin/curl --fail http://localhost:8080/telemetry
    '';
}

{pkgs, ...}:
{
    processes.snippet.exec = "opentelemetry-instrument flask --app snippet_zero.py run -p 5001";
    processes.snippet.process-compose.environment = [  "OTEL_SERVICE_NAME=flask-zero-code" ];

    enterShell = ''
        uv pip install -r requirements.txt
        opentelemetry-bootstrap -a install
    '';

    enterTest = ''
        wait_for_port 5001
        curl --fail http://localhost:5001/rolldice
        curl http://localhost:5001/404
    '';
}

{pkgs, ...}:
{
    processes.snippet_zero.exec = "opentelemetry-instrument flask --app snippet_zero.py run -p 5001";
    processes.snippet_zero.process-compose.environment = [  "OTEL_SERVICE_NAME=flask-zero-code" ];

    enterShell = ''
        uv pip install -r requirements.txt
        opentelemetry-bootstrap -a requirements | uv pip install --requirement -
    '';

    enterTest = ''
        wait_for_port 5001
        curl --fail http://localhost:5001/rolldice
        curl http://localhost:5001/404
    '';
}

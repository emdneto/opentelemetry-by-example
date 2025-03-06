{pkgs, ...}:
{
    processes.snippet_uvicorn.exec = "opentelemetry-instrument uvicorn snippet_uvicorn:app --port 3000 --workers 1";
    processes.snippet_uvicorn.process-compose.environment = [  "OTEL_SERVICE_NAME=fastapi-uvicorn-zero-code" ];

    enterShell = ''
        echo "testing"
        uv pip install -r requirements.txt
        opentelemetry-bootstrap -a requirements | uv pip install --requirement -
    '';

    enterTest = ''
        wait_for_port 3000
        ${pkgs.curl}/bin/curl --fail http://localhost:3000/foobar
    '';
}

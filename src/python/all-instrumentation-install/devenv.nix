{pkgs, ...}:
{
    env.OTEL_SERVICE_NAME = "all-instrumentation-install";

    packages = [pkgs.postgresql pkgs.libmysqlclient ];
    enterShell = ''
        uv pip install -r requirements.txt
    '';

    enterTest = ''
        opentelemetry-instrument --service_name=snippet python snippet.py
    '';
}

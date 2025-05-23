{pkgs, ...}:
{
    # processes.snippet.exec = "opentelemetry-instrument flask --app snippet.py run -p 5001";
    # processes.snippet.process-compose.environment = [  "OTEL_SERVICE_NAME=flask-zero-code" ];

    enterShell = ''
        uv pip install -r requirements.txt
        opentelemetry-bootstrap -a requirements | uv pip install --requirement -
    '';

    enterTest = ''
        python snippet_manual.py
        opentelemetry-instrument --service_name=snippet-zerocode python snippet_zerocode.py
        OTEL_SEMCONV_STABILITY_OPT_IN="http" opentelemetry-instrument --service_name=snippet-zerocode-stable-semconv python snippet_zerocode.py
    '';
}

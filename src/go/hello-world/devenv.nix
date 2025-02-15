{
  # tasks = {
  #       "snippet:setup" = {
  #           exec = ''
  #               uv pip install -r requirements.txt
  #           '';
  #           after = [ "devenv:enterShell" ];
  #       };
  #   };
  enterShell = ''
    go get go.opentelemetry.io/otel
    go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc
    go get go.opentelemetry.io/otel/sdk
    go get go.opentelemetry.io/otel/trace
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    # if ! python snippet_console.py | grep -q "HelloWorldSpan"; then
    #   echo "Error: 'HelloWorldSpan' not found in the output."
    #   exit 1
    # fi

    go run ./snippet_grpc/
  '';
}

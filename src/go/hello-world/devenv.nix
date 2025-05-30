{
  enterShell = ''
# --8<-- [start:deps]
go get go.opentelemetry.io/otel
go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc
go get go.opentelemetry.io/otel/sdk
go get go.opentelemetry.io/otel/trace
# --8<-- [end:deps]
  '';

  enterTest = ''
    # if ! python snippet_console.py | grep -q "HelloWorldSpan"; then
    #   echo "Error: 'HelloWorldSpan' not found in the output."
    #   exit 1
    # fi

    go run ./snippet_grpc/
  '';
}

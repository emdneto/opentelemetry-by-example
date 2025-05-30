---
tags: ["basics"]
---

# Hello World (Traces, Metrics, Logs)

A simple python console application instrumented with OpenTelemetry that generates a span and metrics in some scenarios.

## Setup environment

{{ otel_tui_tip() }}

### Install packages

``` go linenums="1" title="snippet.go"
--8<-- "src/go/hello-world/devenv.nix:deps"
```

## Traces

=== "OTLP gRPC Exporter"

    ``` go linenums="1" title="snippet.go"
    --8<-- "src/go/hello-world/snippet_grpc/snippet.go"
    ```

    !!! tip "Run this snippet"
        ```
        go run ./snippet_grpc/
        ```

## Metrics

!!! bug "TODO"

    In Development


## Logs

!!! bug "TODO"

    In Development

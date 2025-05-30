---
tags: ["basics"]
---

# Hello World (Traces, Metrics, Logs)

A simple Java console application instrumented with OpenTelemetry that generates a span, metrics and logs and exports them to Collector.

## Setup environment

{{ otel_tui_tip() }}

### Install packages

``` gradle linenums="1" title="build.gradle.kts"
--8<-- "src/java/hello-world/build.gradle.kts"
```

## Traces

=== "OTLP gRPC Exporter"

    ``` java linenums="1" title="TracesGrpc.java"
    --8<-- "src/java/hello-world/src/main/java/snippets/TracesGrpc.java"
    ```

    !!! tip "Run this snippet"
        ```
        gradle shadowJar
        java -cp build/libs/hello-world-all.jar snippets.TracesGrpc
        ```

=== "Console Exporter"

    ``` java linenums="1" title="TracesConsole.java"
    --8<-- "src/java/hello-world/src/main/java/snippets/TracesConsole.java"
    ```

    !!! tip "Run this snippet"
        ```
        gradle shadowJar
        java -cp build/libs/hello-world-all.jar snippets.TracesConsole
        ```

## Metrics

!!! bug "TODO"

    In Development

## Logs

!!! bug "TODO"

    In Development

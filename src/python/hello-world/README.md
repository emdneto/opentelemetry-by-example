---
tags: ["basics"]
---

# Hello World (Traces, Metrics, Logs)

A simple python console application instrumented with OpenTelemetry that generates a span and metrics in some scenarios.

## Setup environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("hello-world") }}

## Traces

=== "Console"

    {{ python_run_snippet("hello-world/snippet_console.py")}}

=== "OTLP gRPC Exporter"

    {{ python_run_snippet("hello-world/snippet_grpc.py")}}

=== "OTLP HTTP Exporter"

    {{ python_run_snippet("hello-world/snippet_http.py")}}

## Metrics

=== "Console"

    {{ python_run_snippet("hello-world/snippet_metrics_console.py")}}

=== "OTLP gRPC Exporter"

    {{ python_run_snippet("hello-world/snippet_metrics_grpc.py")}}

=== "OTLP HTTP Exporter"

    {{ python_run_snippet("hello-world/snippet_metrics_http.py")}}

## Logs

!!! bug "TODO"

    In Development
<!-- === "Console"

    {{ python_run_snippet("hello-world/snippet_logs_console.py", "Run the logs console example")}}

=== "OTLP gRPC Exporter"

    {{ python_run_snippet("hello-world/snippet_logs_grpc.py", "Run the logs gRPC example")}}

=== "OTLP HTTP Exporter"

    {{ python_run_snippet("hello-world/snippet_logs_http.py", "Run the logs HTTP example")}} -->

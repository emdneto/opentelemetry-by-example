# Python - Hello World

A simple python console application instrumented with OpenTelemetry that generates a span and metrics in some scenarios:

## Configuring environment

Install the following packages:

```python,install_deps
{{#include requirements.txt}}
```

Start your collector:

```shell
docker run -p 4317:4317 -p 4318:4318 otel/opentelemetry-collector
```

## Traces

### Basic Console Exporter (only for debug purposes)

```python
{{#include snippet_console.py}}
```

### Basic OTLP gRPC Exporter

```python
{{#include snippet_grpc.py}}
```

### Basic OTLP HTTP Exporter

```python
{{#include snippet_http.py}}
```

## Metrics


## Logs

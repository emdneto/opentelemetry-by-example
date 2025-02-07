# Python - Hello World

A simple python console application instrumented with OpenTelemetry that generates a span in some scenarios:

1. [Console (for debug purposes)](#console----writing-the-code)
2. [OpenTelemetry Protocol (OTLP) via gRPC]()
3. [OpenTelemetry Protocol (OTLP) via HTTP]()

### Configuring environment

Install the following python packages:

```python,install_deps
{{#include requirements.txt}}
```

Start your collector:

```shell
docker run -p 4317:4317 -p 4318:4318 otel/opentelemetry-collector
```

### Console Exporter

```python
{{#include snippet_console.py}}
```

### OTLP Exporter gRPC

```python
{{#include snippet_grpc.py}}
```

### OTLP Exporter HTTP

```python
{{#include snippet_http.py}}
```

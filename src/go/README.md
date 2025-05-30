# Getting Started with OpenTelemetry Go

[![Test Go Snippets](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/go.yml/badge.svg)](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/go.yml)
[![Minimum Go Version](https://img.shields.io/github/go-mod/go-version/open-telemetry/opentelemetry-go)](https://go.dev/doc/install)

Snippets that will guide you through instrumenting Go applications with [OpenTelemetry Go API and SDK](https://opentelemetry.io/docs/languages/go/). You'll learn how to implement both manual and automatic instrumentation to emit traces, metrics, and logs to console/OTLP backends.

## OpenTelemetry Go in a nutshell

* [x] [opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go) :material-arrow-right: main repository which implements and delivers the core packages:
    * [ ] [go.opentelemetry.io/otel](https://pkg.go.dev/go.opentelemetry.io/otel) - Core API for creating telemetry data
    * [ ] [go.opentelemetry.io/otel/sdk](https://pkg.go.dev/go.opentelemetry.io/otel/sdk) - Default SDK implementation
    * [ ] [go.opentelemetry.io/otel/semconv](https://pkg.go.dev/go.opentelemetry.io/otel/semconv) - Standard attribute keys and values
    * [ ] [go.opentelemetry.io/otel/exporters/otlp](https://pkg.go.dev/go.opentelemetry.io/otel/exporters/otlp) - OTLP protocol exporters
* [x] [opentelemetry-go-contrib](https://github.com/open-telemetry/opentelemetry-go-contrib) :material-arrow-right: contrib repository which implements and delivers auto-instrumentation, instrumentation packages and custom implementations:
    * [ ] [go.opentelemetry.io/contrib/instrumentation](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation) - Auto-instrumentation for popular Go libraries
    * [ ] [go.opentelemetry.io/contrib/detectors](https://pkg.go.dev/go.opentelemetry.io/contrib/detectors) - Resource detectors for various environments

## Prerequisites

Before starting with this tutorial, ensure you have the following tools installed on your system:

- [X] **Go** - The Go programming language
  * Download from [go.dev](https://go.dev/doc/install)
  * Or install via package manager: `brew install go` (macOS) or `apt install golang-go` (Ubuntu)

- [X] **Docker** - For running OpenTelemetry Collector and observability backends
  * Download from [docker.com](https://www.docker.com/get-started/)

## List of snippets

Following is a list of all available OpenTelemetry Go snippets:
<!-- material/tags { scope: true } -->

---

**Congratulations!** You now have a solid foundation for instrumenting Go applications with OpenTelemetry. Start with the simple examples and gradually add more sophisticated instrumentation as your observability needs grow.

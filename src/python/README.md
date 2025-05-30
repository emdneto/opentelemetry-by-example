# Getting Started with OpenTelemetry Python

[![Test Python Snippets](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/python.yml/badge.svg)](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/python.yml)
[![Minimum Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)

Snippets that will guide you through instrumenting Python applications with [OpenTelemetry Python SDK](https://opentelemetry.io/docs/languages/python/). You'll learn how to implement both manual and automatic instrumentation to emit traces, metrics, and logs to console/OTLP backends.

## OpenTelemetry Python in a nutshell

* [x] [opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python) :material-arrow-right: main repository which implements and delivers the core packages:
    * [ ] [opentelemetry-api](https://pypi.org/project/opentelemetry-api/) - Core API for creating telemetry data
    * [ ] [opentelemetry-sdk](https://pypi.org/project/opentelemetry-sdk/) - Default SDK implementation
    * [ ] [opentelemetry-semantic-conventions](https://pypi.org/project/opentelemetry-semantic-conventions/) - Standard attribute keys and values
    * [ ] [opentelemetry-proto](https://pypi.org/project/opentelemetry-proto/) - Protocol buffer definitions
    * [ ] [opentelemetry-exporter-otlp](https://pypi.org/project/opentelemetry-exporter-otlp/) - OTLP protocol exporters
* [x] [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib) :material-arrow-right: contrib repository which implements and delivers auto-instrumentation, instrumentation packages and custom implementations of exporters, resource detectors and etc:
    * [ ] [opentelemetry-instrumentation](https://pypi.org/project/opentelemetry-instrumentation/) - Auto-instrumentation utilities
    * [ ] [opentelemetry-distro](https://pypi.org/project/opentelemetry-distro/) - Meta-package for easy installation

## Prerequisites

Before starting with this tutorial, ensure you have the following tools installed on your system:

- [X] **uv** - Fast Python package installer and resolver (recommended alternative to pip)
    * Install via curl: `curl -LsSf https://astral.sh/uv/install.sh | sh`
    * Or via pip: `pip install uv`

- [X] **Docker** - For running OpenTelemetry Collector and observability backends
    * Download from [docker.com](https://www.docker.com/get-started/)

## List of snippets

Following is a list of all available OpenTelemetry Python snippets:
<!-- material/tags -->

---

**Congratulations!** You now have a solid foundation for instrumenting Python applications with OpenTelemetry. Start with the simple examples and gradually add more sophisticated instrumentation as your observability needs grow.

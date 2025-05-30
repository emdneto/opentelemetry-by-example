# Getting Started with OpenTelemetry Java

[![Test Java Snippets](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/java.yml/badge.svg)](https://github.com/emdneto/opentelemetry-by-example/actions/workflows/java.yml)
[![Minimum Java Version](https://img.shields.io/badge/java-17-blue.svg)](https://adoptium.net/)

Snippets that will guide you through instrumenting Java applications with [OpenTelemetry Java SDK](https://opentelemetry.io/docs/languages/java/). You'll learn how to implement both manual and automatic instrumentation to emit traces, metrics, and logs to console/OTLP backends.

## OpenTelemetry Java in a nutshell

* [x] [opentelemetry-java](https://github.com/open-telemetry/opentelemetry-java) :material-arrow-right: main repository which implements and delivers the core packages:
    * [ ] [io.opentelemetry:opentelemetry-api](https://mvnrepository.com/artifact/io.opentelemetry/opentelemetry-api) - Core API for creating telemetry data
    * [ ] [io.opentelemetry:opentelemetry-sdk](https://mvnrepository.com/artifact/io.opentelemetry/opentelemetry-sdk) - Default SDK implementation
    * [ ] [io.opentelemetry:opentelemetry-semconv](https://mvnrepository.com/artifact/io.opentelemetry/opentelemetry-semconv) - Standard attribute keys and values
    * [ ] [io.opentelemetry:opentelemetry-exporter-otlp](https://mvnrepository.com/artifact/io.opentelemetry/opentelemetry-exporter-otlp) - OTLP protocol exporters
* [x] [opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation) :material-arrow-right: Java agent for automatic instrumentation:
    * [ ] [opentelemetry-javaagent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases) - Java agent for zero-code instrumentation
    * [ ] [library instrumentations](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation) - Manual instrumentation for popular Java libraries

## Prerequisites

Before starting with this tutorial, ensure you have the following tools installed on your system:

- [X] **Java** - Java Development Kit (JDK 17 or later)
  * Install via package manager: `brew install openjdk` (macOS) or `apt install openjdk-17-jdk` (Ubuntu)

- [X] **Gradle** - Build automation tool (optional, as projects include Gradle wrapper)
  * Download from [gradle.org](https://gradle.org/install/)
  * Or install via package manager: `brew install gradle` (macOS)

- [X] **Docker** - For running OpenTelemetry Collector and observability backends
  * Download from [docker.com](https://www.docker.com/get-started/)

## List of snippets

Following is a list of all available OpenTelemetry Java snippets:
<!-- material/tags { scope: true } -->

---

**Congratulations!** You now have a solid foundation for instrumenting Java applications with OpenTelemetry. Start with the simple examples and gradually add more sophisticated instrumentation as your observability needs grow.

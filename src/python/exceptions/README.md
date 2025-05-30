---
tags: ["basics"]
---

# Recording Errors and Status

A Python application demonstrating OpenTelemetry error handling, status codes, and exception tracking across spans.

## Configuring environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("exceptions") }}

## Recording Exceptions

=== "Recording Exceptions with Attributes"

    {{ python_run_snippet("exceptions/snippet_manual.py")}}

=== "Context Manager"

    {{ python_run_snippet("exceptions/snippet_contextmanager.py")}}

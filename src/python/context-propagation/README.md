---
tags: ["basics"]
---
# Context Propagation

This section contains snippets demonstrating OpenTelemetry context propagation in Python, both within the same process (intra-process) and across different processes (inter-process).

## Configuring environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("context-propagation") }}

## Propagate API

=== "Intra-Process"

    {{ python_run_snippet("context-propagation/snippet_intraprocess.py")}}

=== "Inter-Process"

    {{ python_run_snippet("context-propagation/snippet_interprocess.py")}}

## TraceContextTextMapPropagator

!!! bug "TODO"

    In Development

## W3CBaggagePropagator

!!! bug "TODO"

    In Development

## B3

!!! bug "TODO"

    In Development

## Jaeger

!!! bug "TODO"

    In Development

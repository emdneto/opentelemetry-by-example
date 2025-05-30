---
tags: ["fastapi"]
---
# FastAPI Instrumentation

Snippets related to FastAPI python package

## Configuring environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("fastapi") }}

```
opentelemetry-bootstrap -a requirements | uv pip install -r -
```

## Zero-code Instrumentation

=== "Uvicorn"

    ``` py linenums="1" title="snippet_uvicorn_auto.py"
    --8<-- "src/python/fastapi/snippet_uvicorn_auto.py"
    ```

    !!! tip "Run this snippet"
        ```
        opentelemetry-instrument --service_name=fastapi-uvicorn-zerocode uvicorn snippet_uvicorn_auto:app --port 3000 --workers 1
        ```

## Programmaticaly Auto-Instrumentation

### Using Instrumentors

=== "Uvicorn"

    ``` py linenums="1" title="snippet_uvicorn_manual.py"
    --8<-- "src/python/fastapi/snippet_uvicorn_manual.py:code"
    ```

    !!! tip "Run this snippet"
        ```
        uvicorn snippet_uvicorn_manual:app --port 3000 --workers 1
        ```

### Using Auto-Instrumentation Initialize

=== "Uvicorn"

    {{ python_run_snippet("fastapi/snippet_uvicorn_programmatic.py")}}

## Using Stable HTTP Semantic Conventions

By default `opentelemetry-instrumentation-fastapi` emit telemetry using an old Semantic Convention version.
If you want to use new attributes defined in the OpenTelemetry HTTP Stable Semantic Convetions, you should opt-in as following:

=== "Uvicorn"

    ``` py linenums="1" title="snippet_uvicorn_auto.py"
    --8<-- "src/python/fastapi/snippet_uvicorn_auto.py"
    ```

    !!! tip "Run this snippet"
        ```
        OTEL_SEMCONV_STABILITY_OPT_IN="http" opentelemetry-instrument --service_name fastapi-semconv uvicorn snippet_uvicorn_auto:app --port 3000 --workers 1
        ```

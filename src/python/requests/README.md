---
tags: ["requests"]
---
# Requests Instrumentation

Snippets related to Requests python package

## Configuring environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("requests") }}

```
opentelemetry-bootstrap -a requirements | uv pip install -r -
```

## Zero-code Instrumentation

=== "Snippet"

    ``` py linenums="1" title="snippet_zerocode.py"
    --8<-- "src/python/requests/snippet_zerocode.py"
    ```

    !!! tip "Run this snippet"
        ```
        pentelemetry-instrument --service_name=snippet-zerocode python snippet_zerocode.py
        ```

## Using Instrumentors

=== "Snippet"

    {{ python_run_snippet("requests/snippet_manual.py")}}

## Using Stable HTTP Semantic Conventions

By default `opentelemetry-instrumentation-requests` emit telemetry using an old Semantic Convention version.
If you want to use new attributes defined in the OpenTelemetry HTTP Stable Semantic Convetions, you should opt-in as following:

=== "Snippet"

    ``` py linenums="1" title="snippet_zerocode.py"
    --8<-- "src/python/requests/snippet_zercode.py"
    ```

    !!! tip "Run this snippet"
        ```
        OTEL_SEMCONV_STABILITY_OPT_IN="http" opentelemetry-instrument --service_name=snippet-zerocode-stable-semconv python snippet_zerocode.py
        ```

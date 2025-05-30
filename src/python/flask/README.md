---
tags: ["flask"]
---
# Flask Instrumentation

Snippets related to Flask python package

## Configuring environment

{{ otel_tui_tip() }}

### Install packages

{{ python_install_tip_with_requirements("flask") }}

```
opentelemetry-bootstrap -a requirements | uv pip install -r -
```

## Zero-code Instrumentation

=== "Uvicorn"

    ``` py linenums="1" title="snippet_zero.py"
    --8<-- "src/python/flask/snippet_zero.py"
    ```

    !!! tip "Run this snippet"
        ```
        opentelemetry-instrument --service_name=flask-zero-code flask --app snippet_zero.py run -p 5001
        ```

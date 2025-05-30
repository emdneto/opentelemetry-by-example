def define_env(env):
    @env.macro
    def python_run_snippet(snippet: str, description: str = "Run this Python snippet"):
        base_url = env.conf.get('site_url', 'http://localhost:8000/opentelemetry-by-example')
        base_url = base_url.rstrip('/')
        return f"""
    ``` py linenums="1" title="{snippet.split('/')[-1]}"
    --8<-- "src/python/{snippet}:code"
    ```

    !!! tip "{description}"
        ```
        uv run {base_url}/python/{snippet}
        ```"""

    @env.macro
    def python_install_tip_with_requirements(path: str, description: str ="Quick install with uv"):
        base_url = env.conf.get('site_url', 'http://localhost:8000/opentelemetry-by-example')
        base_url = base_url.rstrip('/')
        return f"""

Create the virtual environment and install the dependencies:
```bash
uv venv && source .venv/bin/activate
```

``` title="requirements.txt"
--8<-- "src/python/{path}/requirements.txt"
```

!!! tip "{description}"

    ```bash
    uv pip install -r {base_url}/python/{path}/requirements.txt
    ```"""

    @env.macro
    def otel_tui_tip():
        return """!!! tip "Development Environment"

    You can run [otel-tui](https://github.com/ymtdzzz/otel-tui) as OpenTelemetry Collector, which acts as a terminal OpenTelemetry viewer

    ```bash
    docker run -p 4317:4317 -p 4318:4318 --rm -it --name otel-tui ymtdzzz/otel-tui:latest
    ```"""

    @env.macro
    def python_snippet_code_block(file_path, title=None, language="py", line_numbers=True):
        if title is None:
            title = file_path.split('/')[-1]
        else:
            title = ''
        title_attr = f' title="{title}"'
        linenums_attr = ' linenums="1"' if line_numbers else ''

        return f"""``` {language}{linenums_attr}{title_attr}
--8<-- "{file_path}"
```"""

    env.variables['site_base_url'] = env.conf.get('site_url', 'https://emdneto.github.io/opentelemetry-by-example').rstrip('/')
    env.variables['repo_url'] = env.conf.get('repo_url', 'https://github.com/emdneto/opentelemetry-by-example')

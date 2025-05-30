{
  enterShell = ''
    uv pip install -r requirements.txt
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Testing traces snippets..."
    if ! uv run snippet_console.py | grep -q "HelloWorldSpan"; then
      echo "Error: 'HelloWorldSpan' not found in the output."
      exit 1
    fi

    uv run snippet_grpc.py
    uv run snippet_http.py

    echo "Testing metrics snippets..."
    if ! uv run snippet_metrics_console.py | grep -q "hello_requests_total"; then
      echo "Error: 'hello_requests_total' metric not found in console output."
      exit 1
    fi

    uv run snippet_metrics_grpc.py
    uv run snippet_metrics_http.py

  '';
}

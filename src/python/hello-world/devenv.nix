{
  # tasks = {
  #       "snippet:setup" = {
  #           exec = ''
  #               uv pip install -r requirements.txt
  #           '';
  #           after = [ "devenv:enterShell" ];
  #       };
  #   };
  enterShell = ''
    uv pip install -r requirements.txt
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    if ! python snippet_console.py | grep -q "HelloWorldSpan"; then
      echo "Error: 'HelloWorldSpan' not found in the output."
      exit 1
    fi

    wait_for_port 4317
    wait_for_port 4318
    python snippet_grpc.py
    python snippet_http.py
  '';
}

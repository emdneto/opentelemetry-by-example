{

  # python = {
  #   version = "3.13";
  #   requirements = ./requirements.txt;
  # };

  # this install extra packages if needed
  # packages = with pkgs; [
  #   curl
  #   jq
  # ];

  # this install extra python packages if needed during tests
  # extraTestRequirements = ''

  # '';

  # this will run before snippet cmd - https://devenv.sh/tests/
  enterTest = ''
    if ! python snippet_console.py | grep -q "HelloWorldSpan"; then
      echo "Error: 'HelloWorldSpan' not found in the output."
      exit 1
    fi
  '';

  # snippet cmds which depends on processes (otelcol/sink)
  snippetCmd = ''
    python snippet_grpc.py
    python snippet_http.py
  '';
}

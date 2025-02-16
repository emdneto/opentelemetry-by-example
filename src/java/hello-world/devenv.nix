{
  # tasks = {
  #       "snippet:setup" = {
  #           exec = ''
  #               # echo "afterShell"
  #           '';
  #           after = [ "devenv:enterShell" ];
  #       };
  #   };

  enterShell = ''
    gradle shadowJar
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    java -cp build/libs/hello-world-all.jar snippets.TracesConsole 2>&1 | grep -q "HelloWorldSpanConsole"
    java -cp build/libs/hello-world-all.jar snippets.TracesGrpc
    # TODO: add metrics, logs and zero-code
  '';
}

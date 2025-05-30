{
  enterShell = ''
    uv pip install -r requirements.txt
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    uv run snippet_manual.py
    uv run snippet_contextmanager.py
  '';
}

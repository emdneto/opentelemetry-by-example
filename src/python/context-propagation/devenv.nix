{
  enterShell = ''
    uv pip install -r requirements.txt
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    uv run snippet_interprocess.py
    uv run snippet_intraprocess.py
  '';
}

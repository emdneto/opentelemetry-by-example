{ pkgs, inputs, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  sink = ./sink;
  snippetTestUtils = ./snippet-test-utils;
  # We need that file to able to install snippetTestUtils in the venv
  testRequirements = pkgs.writeText "test-requirements.txt" ''
    pip
    pyright
    mypy
    ruff
    pytest
    -e ${snippetTestUtils}
  '';
in
{

  languages.python = {
    enable = true;
    package = nixpkgs-unstable.python313;
    venv.enable = true;
    uv.enable = true;
    uv.package = nixpkgs-unstable.uv;
    venv.requirements = ''
      -r ${testRequirements}
    '';
  };

  scripts.run-tests.exec = "pytest";
  scripts.lint.exec = ''
    echo "• Running ruff"
    ruff check --fix
    ruff format
    echo "• Running pyright"
    pyright
    echo "• Running mypy"
    mypy .
  '';

  enterTest = ''
    run-tests
  '';

}

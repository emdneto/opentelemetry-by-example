{ pkgs, inputs, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  snippetTestUtils = ./snippet-test-utils;
  testRequirements = pkgs.writeText "test-requirements.txt" ''
    pyright
    mypy
    ruff
  '';
in
{

  imports = [./base.nix];

  # https://devenv.sh/supported-languages/python/
  languages.python = {
    # we are using the defaults from ./base.nix but can customize this

    # enable = true;
    # package = nixpkgs-unstable.python313;
    # venv.enable = true;
    # uv.enable = true;
    # uv.package = nixpkgs-unstable.uv;
    venv.requirements = ''
      -r ${testRequirements}
    '';
  };

  scripts.lint.exec = ''
    echo "• Running ruff"
    ruff check --fix
    ruff format
    echo "• Running pyright"
    pyright
    echo "• Running mypy"
    mypy .
  '';

  # run-tests is defined at ./base.nix
  enterTest = ''
    run-tests
  '';

}

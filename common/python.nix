{ pkgs, config, inputs, lib, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  sink = ./sink;
  snippetTestUtils = ./snippet-test-utils;
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

    enterShell = ''
      echo
      echo [opentelemetry-by-example] Entering shell
      echo "••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••"
      echo
      echo Available commands:
      echo "••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••"
      echo
      ${pkgs.gnused}/bin/sed -e 's| |••|g' -e 's|=| |' <<EOF | ${pkgs.util-linuxMinimal}/bin/column -t | ${pkgs.gnused}/bin/sed -e 's|^|- |' -e 's|••| |g'
      ${lib.generators.toKeyValue {} (lib.mapAttrs (name: value: value.description) config.scripts)}
      EOF
      echo
  '';

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

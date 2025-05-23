{ pkgs, inputs, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
in
{

  # https://devenv.sh/supported-languages/go/
  languages.go.enable = true;
  #languages.go.package = nixpkgs-unstable.go;

  scripts.lint.exec = ''
    echo "• Running lint"
  '';

  enterTest = ''
    run-tests
  '';

}

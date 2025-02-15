{ pkgs, inputs, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
in
{

  imports = [./base.nix];

  languages.go.enable = true;
  languages.go.package = nixpkgs-unstable.go;

  scripts.lint.exec = ''
    echo "• Running lint"
  '';

  enterTest = ''
    run-tests
  '';

}

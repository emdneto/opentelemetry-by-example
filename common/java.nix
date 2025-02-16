{ pkgs, inputs, config, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
in
{

  imports = [./base.nix];

  # https://devenv.sh/supported-languages/java/#languagesjavaenable
  languages.java = {
    enable = true;
    jdk.package = nixpkgs-unstable.jdk23;
    gradle.package = nixpkgs-unstable.gradle_8;
    gradle.enable = true;
    maven.enable = true;
  };

  scripts.lint.exec = ''
    echo "• Running lint"
  '';

  enterTest = ''
    run-tests
  '';

}

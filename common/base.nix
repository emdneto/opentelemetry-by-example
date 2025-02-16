{ pkgs, inputs, lib, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  snippetTestUtils = ./snippet-test-utils;
in
{

  languages.python = {
    enable = true;
    package = nixpkgs-unstable.python313;
    venv.enable = true;
    uv.enable = true;
    uv.package = nixpkgs-unstable.uv;
    venv.requirements = ''
      pytest
      -e ${snippetTestUtils}
    '';
  };

  scripts.run-tests.exec = "pytest -p no:cacheprovider";

}

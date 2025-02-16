{ pkgs, inputs, lib, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  snippetTestUtils = ./snippet-test-utils;
in
{

  languages.python = {
    enable = true;
    package = pkgs.python313;
    venv.enable = true;
    uv.enable = true;
    uv.package = pkgs.uv;
    venv.requirements = ''
      pytest
      -e ${snippetTestUtils}
    '';
  };

  scripts.run-tests.exec = "pytest -p no:cacheprovider";

}

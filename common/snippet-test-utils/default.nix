{ lib, python3Packages }:
with python3Packages;
buildPythonApplication {
  pname = "snippet-test-utils";
  version = "0.0.0";
  src = ./.;
}

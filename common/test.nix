{ pkgs, lib, config, ...}:

let
  snippetTestUtils = ./snippet-test-utils;
  extraRequirements = pkgs.writeText "requirements.txt" (toString (
    if lib.isPath config.extraTestRequirements
    then builtins.readFile config.extraTestRequirements
    else config.extraTestRequirements
  ));
in
{
  options.extraTestRequirements = lib.mkOption {
      type = lib.types.nullOr (lib.types.either lib.types.lines lib.types.path);
      default = null;
      description = "Extra test requirements to use with alongside with pytest";
    };

  config = {
    packages = [pkgs.uv];
    enterTest = lib.mkAfter ''
        ${pkgs.uv}/bin/uv run --no-project --with pytest --with-editable ${snippetTestUtils} pytest
    '';
  };
}

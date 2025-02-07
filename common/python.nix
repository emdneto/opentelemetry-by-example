{ pkgs, lib, config, ...}:

let
  pythonVersion = lib.replaceStrings ["."] [""] config.python.version;
  pythonPkg = pkgs."python${pythonVersion}";
  venvDir = "${config.env.DEVENV_STATE}/.venv";
  snippetTestUtils = ./snippet-test-utils;
  testRequirements = pkgs.writeText "test-requirements.txt" ''
    pyright
    mypy
    ruff
    -e ${snippetTestUtils}
  '';
in
{
  imports = [
    ./test.nix
  ];
  options.python = {
    version = lib.mkOption {
      type = lib.types.str;
      default = "3.13";
      description = "Python version to use";
    };

    requirements = lib.mkOption {
      type = lib.types.path;
      default = "${config.env.DEVENV_ROOT}/requirements.txt";
      description = "Path to requirements.txt";
    };
  };

  options.snippetCmd = lib.mkOption {
      type = lib.types.str;
      default = "python snippet.py";
      description = "Command to run snippets";
    };

  config = {
    packages = [pkgs.uv];

    tasks = {
    "python:setup" = {
      exec = ''
        ${pkgs.uv}/bin/uv venv --seed --python=${config.python.version} --directory=${config.env.DEVENV_STATE}
        source ${venvDir}/bin/activate
        ${pkgs.uv}/bin/uv pip install -r ${config.python.requirements}
        ${pkgs.uv}/bin/uv pip install -r ${testRequirements}
      '';
      before = [ "devenv:enterShell" "devenv:enterTest" ];
    };
    };

    enterShell = ''
        export PATH="${venvDir}/bin:$PATH"
    '';

    scripts.lint.exec = ''
      echo "• Running ruff"
      ruff check --fix
      ruff format
      echo "• Running pyright"
      pyright
    '';

    enterTest = ''
        wait_for_port 8080
        wait_for_port 4319
        wait_for_port 4317
        wait_for_port 4318
        ${config.snippetCmd}
    '';
  };
}

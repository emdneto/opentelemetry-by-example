{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    venv.enable = true;
    uv.enable = true;
  };

  packages = with pkgs; [
    mdbook
    git
  ];


  # https://devenv.sh/packages/


  # https://devenv.sh/languages/
  # languages.rust.enable = true;

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/

  enterShell = ''

  '';
  scripts.clean.exec = ''
    devenv gc
    find . -name ".devenv*" -exec rm -rf {} +
    find . -name ".*_cache" -exec rm -rf {} +
    find . -name "__pycache__" -exec rm -rf {} +
  '';

  scripts.update-locks.exec = ''
    find . -type f -name "devenv.nix" -exec sh -c 'pushd "$(dirname "$1")" && devenv update' _ {} \;
  '';

  scripts.rund.exec = ''
    SNIPPET_DIR=src/$1
    pushd $SNIPPET_DIR && devenv ci -d && popd
  '';

  scripts.run.exec = ''
    SNIPPET_DIR=src/$1
    pushd $SNIPPET_DIR && devenv ci && popd
  '';

  scripts.enter.exec = ''
    SNIPPET_DIR=src/$1
    pushd $SNIPPET_DIR && devenv shell && popd
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  # enterTest = ''
  #   echo "Running tests"
  #   git --version | grep --color=auto "${pkgs.git.version}"
  # '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}

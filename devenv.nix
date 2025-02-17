{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    venv.enable = true;
    uv.enable = true;
  };

  languages.go = {
    enable = true;
  };

  packages = with pkgs; [
    hugo
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
    find . -type d \(
        -name ".devenv*"
        -o -name ".*_cache"
        -o -name "__pycache__"
        -o -name "build"
        -o -name ".gradle"
    \) -exec rm -rf {} +
  '';

  scripts.auto-update.exec = ''
    find src/ -type f -name "devenv.nix" -exec sh -c 'pushd "$(dirname "$1")" && devenv update' _ {} \;
  '';

  scripts.hugo-dev.exec = "hugo server --buildDrafts --disableFastRender";
  scripts.hugo-build.exec = ''hugo --gc --minify --baseURL "$1/"'';

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

{ pkgs, inputs, ...}:
let
  nixpkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };
  kindFile = ./kind.yaml;
  certManagerversion = "v1.17.0";
in
{
  packages = [
    nixpkgs-unstable.kind
    nixpkgs-unstable.kubectl
  ];


    tasks = {
        "kind:setup" = {
            exec = ''
                ${pkgs.kind}/bin/kind create cluster --config ${kindFile}
                until ${pkgs.kubectl}/bin/kubectl get nodes &> /dev/null; do
                    echo "Waiting for Kind cluster to be ready..."
                    sleep 2
                done

                echo "Kind cluster is ready!"
                ${pkgs.kubectl}/bin/kubectl wait pods -n kube-system -l tier=control-plane --for condition=Ready --timeout=90s
                ${pkgs.kubectl}/bin/kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/${certManagerversion}/cert-manager.yaml
                ${pkgs.kubectl}/bin/kubectl wait pods -n cert-manager --for condition=Ready --timeout=120s
                ${pkgs.kubectl}/bin/kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/latest/download/opentelemetry-operator.yaml
                ${pkgs.kubectl}/bin/kubectl wait pods -n opentelemetry-operator-system --for condition=Ready --timeout=120s
            '';
            after = [ "devenv:enterTest" ];
        };
    };
  scripts.lint.exec = ''
    echo "• Running lint"
  '';


  enterTest = ''
    run-tests
    kind delete cluster --name obe
  '';

}

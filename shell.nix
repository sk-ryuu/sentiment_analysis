# We use Nix to pin Python and other system packages for consistency;
# and a Python virtual environment for Python packages for more flexibility.
# https://nixos.wiki/wiki/Python

let
  isNixOS = builtins.pathExists /etc/nixos;
  pkgs = import ( # nixpkgs 22.05
    builtins.fetchTarball "https://github.com/NixOS/nixpkgs/archive/ce6aa13369b667ac2542593170993504932eb836.tar.gz"
  ) {};
in (pkgs.buildFHSUserEnv {
  name = "nutshell";

  targetPkgs = pkgs: with pkgs; [
    git
    wget
    curl
    which
    openssh
    pre-commit
    python3
    python3.pkgs.pip
  ]
  # Need `nixGL` on non-NixOS for CUDA access.
  ++ pkgs.lib.optionals (!isNixOS) [
    (import (
      builtins.fetchTarball "https://github.com/guibou/nixGL/archive/7165ffbccbd2cf4379b6cd6d2edd1620a427e5ae.tar.gz"
    ) {}).auto.nixGLDefault
  ];

  profile = ''
    git config --global --add safe.directory $(pwd)
    python -m venv .venv
    source .venv/bin/activate

    export TMPDIR=/var/tmp
    pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu116

    pre-commit install
  '';
}).env

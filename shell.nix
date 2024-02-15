{ pkgs ? import <nixpkgs> {
    config.allowUnfree = true;
} }:

let
    gdk = pkgs.google-cloud-sdk.withExtraComponents (with pkgs.google-cloud-sdk.components; [
        gke-gcloud-auth-plugin
    ]);
in
pkgs.mkShell {
    name="dev";
    buildInputs = with pkgs; [
        gnumake
        docker-compose
        nodejs_21
        terraform
        gdk
        black
        ffmpeg
        libGL
        libGL.dev
        python311Packages.opencv4 
        python311Packages.pip
    ];

    shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.libGL}/lib:${pkgs.libGLU}/lib:${pkgs.freeglut}/lib:${pkgs.xorg.libX11}/lib:${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.cudatoolkit_11}/lib:${pkgs.cudatoolkit_11.lib}/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=$(nixGLNvidia printenv LD_LIBRARY_PATH):$LD_LIBRARY_PATH
    echo "Let's go"
    '';
}

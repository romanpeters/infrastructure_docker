# Auto-generated using compose2nix v0.2.1.
{ pkgs, lib, ... }:

{
  # Runtime
  virtualisation.podman = {
    enable = true;
    autoPrune.enable = true;
    dockerCompat = true;
    defaultNetwork.settings = {
      # Required for container networking to be able to use names.
      dns_enabled = true;
    };
  };
  virtualisation.oci-containers.backend = "podman";

  # Containers
  virtualisation.oci-containers.containers."homebox" = {
    image = "ghcr.io/hay-kot/homebox:v0.10.3";
    environment = {
      "HBOX_LOG_FORMAT" = "text";
      "HBOX_LOG_LEVEL" = "info";
      "HBOX_WEB_MAX_UPLOAD_SIZE" = "10";
    };
    volumes = [
      "/Users/romanpeters/Developer/infrastructure_docker/homebox/data:/data:rw"
    ];
    ports = [
      "8002:7745/tcp"
    ];
    log-driver = "journald";
    extraOptions = [
      "--network-alias=homebox"
      "--network=homebox_default"
    ];
  };
  systemd.services."podman-homebox" = {
    serviceConfig = {
      Restart = lib.mkOverride 500 "always";
    };
    after = [
      "podman-network-homebox_default.service"
    ];
    requires = [
      "podman-network-homebox_default.service"
    ];
    partOf = [
      "podman-compose-homebox-root.target"
    ];
    wantedBy = [
      "podman-compose-homebox-root.target"
    ];
  };

  # Networks
  systemd.services."podman-network-homebox_default" = {
    path = [ pkgs.podman ];
    serviceConfig = {
      Type = "oneshot";
      RemainAfterExit = true;
      ExecStop = "podman network rm -f homebox_default";
    };
    script = ''
      podman network inspect homebox_default || podman network create homebox_default
    '';
    partOf = [ "podman-compose-homebox-root.target" ];
    wantedBy = [ "podman-compose-homebox-root.target" ];
  };

  # Root service
  # When started, this will automatically create all resources and start
  # the containers. When stopped, this will teardown all resources.
  systemd.targets."podman-compose-homebox-root" = {
    unitConfig = {
      Description = "Root target generated by compose2nix.";
    };
    wantedBy = [ "multi-user.target" ];
  };
}

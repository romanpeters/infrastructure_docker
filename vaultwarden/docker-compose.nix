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
  virtualisation.oci-containers.containers."vaultwarden" = {
    image = "vaultwarden/server:1.30.1";
    environment = {
      "EXTENDED_LOGGING" = "false";
      "LOG_FILE" = "/data/logs/bitwarden.log";
      "LOG_LEVEL" = "warn";
      "SENDS_ALLOWED" = "true";
      "SIGNUPS_ALLOWED" = "true";
      "WEBSOCKET_ENABLED" = "true";
    };
    volumes = [
      "/Users/romanpeters/Developer/infrastructure_docker/vaultwarden/data:/data:rw"
    ];
    ports = [
      "8004:80/tcp"
      "3012:3012/tcp"
    ];
    log-driver = "journald";
    extraOptions = [
      "--network-alias=vaultwarden"
      "--network=vaultwarden_default"
    ];
  };
  systemd.services."podman-vaultwarden" = {
    serviceConfig = {
      Restart = lib.mkOverride 500 "always";
    };
    after = [
      "podman-network-vaultwarden_default.service"
    ];
    requires = [
      "podman-network-vaultwarden_default.service"
    ];
    partOf = [
      "podman-compose-vaultwarden-root.target"
    ];
    wantedBy = [
      "podman-compose-vaultwarden-root.target"
    ];
  };

  # Networks
  systemd.services."podman-network-vaultwarden_default" = {
    path = [ pkgs.podman ];
    serviceConfig = {
      Type = "oneshot";
      RemainAfterExit = true;
      ExecStop = "podman network rm -f vaultwarden_default";
    };
    script = ''
      podman network inspect vaultwarden_default || podman network create vaultwarden_default
    '';
    partOf = [ "podman-compose-vaultwarden-root.target" ];
    wantedBy = [ "podman-compose-vaultwarden-root.target" ];
  };

  # Root service
  # When started, this will automatically create all resources and start
  # the containers. When stopped, this will teardown all resources.
  systemd.targets."podman-compose-vaultwarden-root" = {
    unitConfig = {
      Description = "Root target generated by compose2nix.";
    };
    wantedBy = [ "multi-user.target" ];
  };
}

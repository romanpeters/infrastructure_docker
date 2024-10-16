---
- name: change
  image: changedetection
  port: 8001
  path: changedetection/change/docker-compose.yml

- name: homebox
  image: homebox
  port: 8002
  path: homebox/homebox/docker-compose.yml

- name: nginx
  image: nginx_proxy_manager
  port: 8003
  path: nginx_proxy_manager/nginx/docker-compose.yml

- name: vaultwarden
  image: vaultwarden
  port: 8004
  path: vaultwarden/vaultwarden/docker-compose.yml

- name: traefik
  image: traefik
  port: 8004
  path: traefik/traefik/docker-compose.yml

- name: adguard
  image: adguardhome
  port: 8005
  path: adguardhome/adguard/docker-compose.yml

- name: hello
  image: heimdall
  port: 8006
  path: heimdall/hello/docker-compose.yml

- name: uptime_kuma_tan
  image: uptime_kuma
  port: 8007
  path: uptime_kuma/uptime_kuma_tan/docker-compose.yml

- name: rtv
  image: heimdall
  port: 8008
  path: heimdall/rtv/docker-compose.yml

- name: tautullli
  image: tautulli
  port: 8009
  path: tautulli/tautullli/docker-compose.yml

- name: request
  image: overseerr
  port: 8010
  path: overseerr/request/docker-compose.yml

- name: start
  image: homepage
  port: 8011
  path: homepage/start/docker-compose.yml

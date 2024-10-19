```
- image: changedetection
  name: change
  path: changedetection/change/docker-compose.yml
  port: '8001'

- image: homebox
  name: homebox
  path: homebox/homebox/docker-compose.yml
  port: '8002'

- image: nginx-proxy-manager
  name: nginx
  path: nginx-proxy-manager/nginx/docker-compose.yml
  port: '8003'

- image: vaultwarden
  name: vaultwarden
  path: vaultwarden/vaultwarden/docker-compose.yml
  port: '8004'

- image: traefik
  name: traefik
  path: traefik/traefik/docker-compose.yml
  port: '8004'

- image: adguardhome
  name: adguard
  path: adguardhome/adguard/docker-compose.yml
  port: '8005'

- image: heimdall
  name: hello
  path: heimdall/hello/docker-compose.yml
  port: '8006'

- image: uptime-kuma
  name: uptime-other
  path: uptime-kuma/uptime-other/docker-compose.yml
  port: '8007'

- image: heimdall
  name: rtv
  path: heimdall/rtv/docker-compose.yml
  port: '8008'

- image: tautulli
  name: tautullli
  path: tautulli/tautullli/docker-compose.yml
  port: '8009'

- image: overseerr
  name: request
  path: overseerr/request/docker-compose.yml
  port: '8010'

- image: homepage
  name: start
  path: homepage/start/docker-compose.yml
  port: '8011'

```
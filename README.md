```yaml
infrastructure_docker:
  - name: change
    image: changedetection
    port: '8001'
    path: changedetection/change
  - name: homebox
    image: homebox
    port: '8002'
    path: homebox/homebox
  - name: nginx
    image: nginx-proxy-manager
    port: '8003'
    path: nginx-proxy-manager/nginx
  - name: vaultwarden
    image: vaultwarden
    port: '8004'
    path: vaultwarden/vaultwarden
  - name: adguard
    image: adguardhome
    port: '8005'
    path: adguardhome/adguard
  - name: hello
    image: heimdall
    port: '8006'
    path: heimdall/hello
  - name: uptime-other
    image: uptime-kuma
    port: '8007'
    path: uptime-kuma/uptime-other
  - name: rtv
    image: heimdall
    port: '8008'
    path: heimdall/rtv
  - name: tautulli
    image: tautulli
    port: '8009'
    path: tautulli/tautulli
  - name: request
    image: overseerr
    port: '8010'
    path: overseerr/request
  - name: start
    image: homepage
    port: '8011'
    path: homepage/start
  - name: app
    image: homepage
    port: '8012'
    path: homepage/app
  - name: traefik
    image: traefik
    port: '8013'
    path: traefik/traefik
  - name: ebooks
    image: calibre-web
    port: '8014'
    path: calibre-web/ebooks
  - name: books
    image: audiobookshelf
    port: '8015'
    path: audiobookshelf/books
```

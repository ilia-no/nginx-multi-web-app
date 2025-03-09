Test

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose certbot python3-certbot-nginx
sudo systemctl enable --now docker
```

```bash
docker --version
docker-compose --version
```

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

```bash
docker-compose up -d
```

```bash
docker-compose run --rm certbot certonly --webroot -w /var/www/certbot \
  --register-unsafely-without-email \
  -d test.been.earth -d test2.been.earth -d test3.been.earth \
  --agree-tos --no-eff-email --force-renewal
```

```bash
docker-compose restart nginx
```


```bash
docker logs nginx_proxy
```
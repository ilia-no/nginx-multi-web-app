
```bash
sudo apt update && sudo apt upgrade -y
```

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
```

```bash
sudo apt install -y docker-compose
```

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

```bash
docker --version
docker-compose --version
```

```bash
cd /srv
git clone https://github.com/ilia-no/nginx-multi-web-app
cd nginx-multi-web-app
docker-compose up -d
docker ps
```


```bash
docker-compose stop nginx
docker run --rm -it \
    -v $(pwd)/certbot/conf:/etc/letsencrypt \
    -v $(pwd)/certbot/www:/var/www/certbot \
    certbot/certbot certonly --standalone \
    # --email your-email@example.com \
    --register-unsafely-without-email \
    -d test.been.earth -d test1.been.earth -d test2.been.earth \
    --agree-tos --no-eff-email --force-renewal
docker-compose start nginx
```

```bash
EDITOR=nano crontab -e
```

```bash
0 3 * * * docker run --rm -v $(pwd)/certbot/conf:/etc/letsencrypt -v $(pwd)/certbot/www:/var/www/certbot certbot/certbot renew --standalone --pre-hook "docker-compose stop nginx" --post-hook "docker-compose start nginx" --quiet
```
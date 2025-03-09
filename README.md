Test

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 certbot python3-certbot-nginx
```

Installing docker

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
```

Installing docker-compose
```bash
sudo apt install -y docker-compose
```

Enabling docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Checking versions of installed packages to make sure they are all installed correctly

```bash
python3 --version
docker --version
```

```bash
docker --version
docker-compose --version
```

```bash
ufw reset
ufw default deny incoming
ufw default allow outgoing

ufw allow http
ufw allow https
ufw allow ssh
ufw enable
ufw reload
ufw status verbose
```


```bash
cd /srv
git clone https://github.com/ilia-no/nginx-multi-web-app
cd nginx-multi-web-app
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
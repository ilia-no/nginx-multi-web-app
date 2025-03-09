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
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d test.been.earth -d test2.been.earth -d test3.been.earth
```

```bash
docker-compose restart
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d test.been.earth -d test2.been.earth -d test3.been.earth
```

```bash
EDITOR=nano crontab -e
```

```bash
0 3 * * * docker-compose run --rm certbot renew
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
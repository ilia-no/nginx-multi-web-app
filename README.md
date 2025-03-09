## Installation

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
```

## The real challenge begins here.
```bash
docker-compose up -d
```

```bash
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d test.been.earth -d test2.been.earth -d test3.been.earth
```

```bash
docker-compose restart
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d test.been.earth -d test2.been.earth -d test3.been.earth
```

## Then we need to enable SSL in the nginx configuration file.

```bash
docker-compose down
```

Now we have to go to "docker-compose.yml" and uncomment the lines with the certificates (See nginx volumes).
It should look like this:

```bash
nano docker-compose.yml
```

```yaml
volumes:
    # - ./nginx/no-ssl.conf:/etc/nginx/nginx.conf:ro # Comment this line after you have SSL
    - ./nginx/ssl.conf:/etc/nginx/nginx.conf:ro # Uncomment this line after you have SSL
    - ./certbot/www:/var/www/certbot/:ro
    - ./certbot/conf/:/etc/nginx/ssl/:ro # Uncomment this line after you have SSL
```

```bash
docker-compose up -d
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
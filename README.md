## Before installation
Configure your Dockerfiles to use the correct ports.
For example:
```bash
./domain1/Dockerfile 8001
./domain2/Dockerfile 8002
./domain2/Dockerfile 8003
```

Configure your nginx configuration to use the correct ports and correct domains.
```bash
./nginx/no-ssl.conf
./nginx/ssl.conf
```

## Installation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 nginx certbot python3-certbot-nginx git
```


## Cloning the repository
```bash
cd /srv
git clone https://github.com/ilia-no/nginx-multi-web-app
cd nginx-multi-web-app
```


## Creating certificates (SSL)
```bash
mv nginx/no-ssl.conf /etc/nginx/sites-available/default
```

Change your domains here
```bash
sudo certbot --nginx --register-unsafely-without-email -d test.been.earth -d test2.been.earth -d test3.been.earth 
sudo certbot renew --dry-run --force-renewal
```

```bash
EDITOR=nano crontab -e
```

```bash
0 3 * * * certbot renew --quiet --post-hook "systemctl reload nginx"
```

```bash
mv nginx/ssl.conf /etc/nginx/sites-available/default
```


## Docker installing

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

## Building and running the project
```bash
docker-compose build
docker-compose up -d
```

## Setting up firewall

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
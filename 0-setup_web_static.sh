#!/usr/bin/env bash
# Prepares web servers for web static deployment

# Install nginx
apt-get update
apt-get -y install nginx

# create directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create fake html landing page
INDEX_JIBB=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo -e "$INDEX_JIBB" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of data folder
chown -fR ubuntu:ubuntu /data/

# Change default landing page
echo "Hello World!" > /var/www/html/index.html

# Create error page
echo "Ceci n'est pas une page" > /var/www/html/404.html

# Update nginx configuration
NEW_CONFIG=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
		add_header X-Served-By \$hostname;
	}

	location /hbnb_static {
		alias /data/web_static/current/;
	}
	error_page 404 /404.html;
	location /404.html {
		internal;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://exmaple.com? permanent;
	}
}"

echo -e "$NEW_CONFIG" > /etc/nginx/sites-enabled/default

# restart nginx and apply updates
service nginx restart

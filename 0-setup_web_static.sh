#!/usr/bin/env bash
# script to setup server

sudo apt-get -y update
sudo apt-get install -y nginx

# create server directories
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html> " | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link 'current' to point to 'test/' folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to user and group 'ubuntu'
sudo chown -R ubuntu:ubuntu /data

# using sed command to updata nginx configuration to serve content to 'hbnb_static'
sudo sed -i '37 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# restart the nginx server
sudo service nginx restart

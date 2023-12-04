#Automate custom server http header creation

exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sed -i "/listen 80 default_server;/a add_header X-Served-By $HostName;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell;
}

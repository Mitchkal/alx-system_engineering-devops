# File: nginx_setup.pp
# sets up nginx server and default pages

# install nginx
package { 'nginx':
  ensure => installed,
}


# defaullt server
file_line{ 'aaaaa':
  ensure => present,
  path   => 'etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGU1wu4 permanent;',
  notify => Service['nginx'],
}

# root block
file { '/var/www/html/index.html':
  ensure   => file
  content  => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

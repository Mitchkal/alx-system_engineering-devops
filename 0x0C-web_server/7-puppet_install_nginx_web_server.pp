# File: nginx_setup.pp
# sets up nginx server and default pages

# install nginx
package { 'nginx':
  ensure => installed,
}

# configure
class { 'nginx':
  listen_port => '80',
}

# defaullt server
nginx::resource::vhost { 'default':
  ensure  => present,
  listen  => ['80 default_server'],
  options => {
    'rewrite' => '^/redirect_me https://www.youtube.com/watch?v=QH2-TGU1wu4 permanent',
  }'
}

# root block
nginx::resource::location { 'root':
  ensure   => present,
  vhost    => 'default',
  location => '/',
  content  => 'Hello World!',
}

# 404 page
nginx:: resource::location { 'error_page_404':
  ensure   => present
  vhost    => 'default'
  location => '/page_error_404.html',
  options  => {
    'internal' => true,
  },
  content => 'Ceci n\'est pas une page',
}


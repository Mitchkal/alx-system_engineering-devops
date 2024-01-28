# Fix nginx too many open files

exec {'modify maximum open file limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => ['/usr/local/bin', '/usr/bin', '/bin']
}

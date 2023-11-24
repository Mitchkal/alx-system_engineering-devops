# Creates a manifest to kill a process killmenow

exec { 'pkill killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true
}

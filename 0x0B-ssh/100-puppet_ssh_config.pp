# configures server to authenticate with public key, no password

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => '
    Host 18.206.197.179
        IdentityFile ~/.ssh/school
        PreferredAuthentications publickey
        PasswordAuthentication no
        User ubuntu
    ',
}
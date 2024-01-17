# Fixes apache error 500 due to isspelling in config
exec { 'fix error in config':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
}

#Command Line for the win
Contains screenshots for completed command line for the win tasks
##Uploading to remote via sftp

	Open a local terminal window or CMD on windows
	sftp to the remote host  using the following command
		sftp username@your_server_ip_or_remote_hostname
	. You can view your current locationin remote once connection is established by:
		pwd
	You can then Navigate to the desired remote directory using:
		cd directory_name\
	Navigate to the local directory containing files to upload using:
		lcd local_directory\
	You can also view files in local directory using:
		lls 
		note that you can also attach some additional arguments like in bash e.g:
			ls -la in the remote terminal
	Upload desired files to remote using the command:
		put file_name
		put is the command to upload , while file_name is argument
	You can close the remote connection using:
			bye

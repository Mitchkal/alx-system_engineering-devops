Exercise 0: pwd === print working directory

Exercise 1: ls === list directory contents

Exercise 2: cd === change directory

Exercise 3: ls -l === list directory contents in long form

Exercise 4: ls -la === list directory contents in long form, including hidden files

Exercise 5: ls -la Note:  files are inherently ordered?

Exercise 6: mkdir /tmp/school Create a school directory inside the tmp directory

Exercise 7: mv /tmp/betty /tmp/school/betty Move file betty, which is inside the tmp directory, to the school directory, which is also located inside the tmp directory

Exercise 8: rm /tmp/school/betty Delete file betty located in tmp/school directory.

Exercise 9: rmdir /tmp/school Remove directory school located in directory tmp.

Exercise 10: cd - Change directory to the previous directory 

Exercise 11: ls -la . .. /boot List all files/directories, including hidden files/directories, from 3 separate directories: current directory, parent of working directory, and /boot directory.ls allows listing multiple directories  separated by spaces.

Exercise 12: file /tmp/iamafile Prints the type of file iamafile.

Exercise 13: ln -s /bin/_ls_ ls Create a symbolic link named _ls_ for /bin/ls

Exercise 14: cp -u *.html .. Copy all html files from the current directory to the parent directoryd, but only copy files that didn't exist in the parent directory or are newer versions.

Exercise 15: mv [[:upper:]]* /tmp/u Move all files that begin with a capital letter to /tmp/u

Exercise 16: rm *~ Deletes all files in the current directory that end with a ~

Exercise 17: mkdir -p welcome/to/school Create directory welcome in current directory. Create directory to inside directory welcome. The -p option creates any intermediate directories in the path argument.

Exercise 18: ls -pam List all files and directories of the current directory, separated by commas. Directory names should end with a /. The listing should be alph ordered, except for dot (.) or dot dot (..), which should be listed at the beginning. The -a option shows any hidden files. The -p writes a / at the end of directory names. The -m option streams output, separating each listing with a comma.

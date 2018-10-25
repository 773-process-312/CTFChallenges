# User flag:
`inspector{hash_cracker_isMD5broken}`

# Root flag:
`inspector{my_first_reverse_shell_super1337}`

# Solution:
The idea with this box is to find the MD5 hash of the password '123qwe' and to log in using this password. Once logged in the player can use the poorly written ping form to inject commands. The challenge can be solved without a reverse shell but the idea is to use netcat to get a simple interactive reverse shell going and to find the 'root' flag at /home/root/root.txt

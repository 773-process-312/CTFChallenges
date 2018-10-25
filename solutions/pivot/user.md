# Pivot User

The CTF scoreboard gives the following information:
```
Host: 10.10.2.1 Username: ctf Password: ReallySecurePassword
```

Running nmap on that IP gives the following output:

```
Starting Nmap 7.60 ( https://nmap.org ) at 2018-10-25 22:54 BST
Nmap scan report for 10.10.2.1
Host is up (0.15s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 3.53 seconds

```

The only service open is SSH, so if we login with credentials given above we
are given a shell.

Running `ls -la` gives us the following output:

```
total 32
drwxr-xr-x 1 ctf  ctf  4096 Oct 16 17:32 .
drwxr-xr-x 1 root root 4096 Oct 13 02:41 ..
-r--r--r-- 1 root root   30 Oct 13 02:45 .bash_history
-rw-r--r-- 1 ctf  ctf   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ctf  ctf  3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 ctf  ctf   807 Apr  4  2018 .profile
drwx------ 2 ctf  ctf  4096 Oct 16 17:32 .ssh
```

As you can see, the file `.bash_history` exists.

`cat`'ing that, gives the following:


```
echo "CTF{now_you_can_pivot}"
```

So we have the flag now.

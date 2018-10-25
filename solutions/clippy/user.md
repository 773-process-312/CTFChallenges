# Clippy (user)

The following information is given by the scoreboard:

```
Host: 10.10.2.3

Should be simple.
```

Running nmap with the `-sV` option on this host gives the following output:

```
Starting Nmap 7.60 ( https://nmap.org ) at 2018-10-25 23:10 BST
Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 1.90% done; ETC: 23:10 (0:00:00 remaining)
Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 21.15% done; ETC: 23:10 (0:00:00 remaining)
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 73.85% done; ETC: 23:10 (0:00:00 remaining)
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 23:10 (0:00:00 remaining)
Stats: 0:00:07 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 23:10 (0:00:06 remaining)
Nmap scan report for 10.10.2.3
Host is up (0.043s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Werkzeug httpd 0.14.1 (Python 2.7.15rc1)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.94 seconds
```

Investigating the service on port 5000 returns a pastebin clone.

When we paste something, we get redirected to our paste, which has a numeric id
in the URL. If we modify the URL we find a paste with the ID of 5
(URL: `http://10.10.2.3:5000/note/5`) that contains login credentials.

```
ssh: 10.10.2.3
user: clippy
password: need_some_help
```

This work for SSH, so we can then get the flag from `user.txt`

```
CTF{quick_maths}
```

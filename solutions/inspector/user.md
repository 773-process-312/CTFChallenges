# Inspector (user)

The scoreboard server gives the following information:

```
Host: 10.10.2.2

Get the flag :)
```

So, we we nmap this host we get given the following:
```
Starting Nmap 7.60 ( https://nmap.org ) at 2018-10-25 23:01 BST
Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 29.10% done; ETC: 23:01 (0:00:00 remaining)
Nmap scan report for 10.10.2.2
Host is up (0.060s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.00 seconds

```

When we connect to the web service, we get given a login page.

Trying a few common logins give nothing.

The pages source has the following comment:
```
<!-- TODO: Stop using hardcoded passwords! And maybe choose a better hashing algo?--><!-- 46f94c8de14fb36680850768ff1b7f2a-->
```

This hints at string being hashed. Googling the hash tells us that is `123qwe`
hashed with MD5.

We then login with `admin/123qwe` and are given the flag:

```
ctf{hash_cracker_isMD5broken}
```

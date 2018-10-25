import json
import time
import hmac
import cPickle
import redis
import base64
import os

from sandbox import Sandbox

# Validate we have a trusted job.
def valid_payload(payload, key):
    try:
        data, mac = payload.split(',')[0:2]
        d = hmac.new(key, data).digest()
        return hmac.compare_digest(d, mac.decode('hex'))
    except:
        return False

def fetch_job(connection, queue):
    # Connect to the redis queue and fetch the latest.
    try:
        return connection.rpop(queue)
    except:
        return None

# Function that runs the user provided input in the sandbox.
def handler(code):
    exec(code)

def evaluate_job(job):
    # Deserialize the job description. Lots that can go wrong here.
    try:
        action = cPickle.loads(base64.b64decode(job))
    except Exception as e:
        print("[!] Deserialize Failed", e)
    try:
        if 'name' not in action or 'description' not in action:
            return None
    except:
        return None
    # run the code in pysandbox. Apparently this can be broken out of, but
    # should be fine for our trusted users.
    sandbox = Sandbox()
    print("[!] Running %s" % action['name'])
    sandbox.call(handler, action['description'])
    print("[!] Finished %s" % action['name'])
    return None

def main(config_file):
    # load config
    with open(config_file, 'r') as open_config:
        config = json.load(open_config)
        # Establish a connection to the redis server.
        connection = redis.Redis(
            host=config['host'],
            port=config['port'],
            password=config['password']
        )
        key = config['key'].decode('hex')
        queue = config['queue']
        # Now do our event loop.
        while True:
            job = fetch_job(connection, queue)
            if job is None:
                time.sleep(5)
                continue
            elif valid_payload(job, key):
                evaluate_job(job)
            else:
                print("[!] Invalid Job!!!!")

if __name__ == "__main__":
    main('./etc/jobs.json')

from flask import Flask
from redis import Redis
import os
import subprocess

host = subprocess.check_output("curl -s http://localhost:8500/v1/catalog/service/redis|cut -c 154-165", shell=True)
#print "program output:", redis

app = Flask(__name__)
redis = Redis(host='redis.service.consul', port=6379)
#host = Redis(host='host', port=6379)
#redis = Redis(host='172.30.100.3', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

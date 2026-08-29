from flask import Flask,jsonify
import datetime, os, time
import socket

app = Flask(__name__)

app.json.compact = False
app.json.sort_keys = False

CONTAINER_START_TIME = os.path.getmtime('/proc/1')

@app.route('/api/v1/details')

def details():
    uptime_seconds = int(time.time() - CONTAINER_START_TIME)
    uptime_string = str(datetime.timedelta(seconds=uptime_seconds))

    return jsonify({
        'local_now' : datetime.datetime.now().astimezone(),
        'hostname': socket.gethostname(),
        'uptime': uptime_string,
        'message': 'you are a good human!'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'up'
        }), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")

#'/api/v1/details'
#'/api/v1/healthz'
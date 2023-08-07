from flask import Flask, request, jsonify
import sys
from flask_cors import CORS
from flask import send_file
import datetime

app = Flask(__name__)
CORS(app)
port = int(sys.argv[1])
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH', 'PROPFIND']

# @app.route("/", methods=HTTP_METHODS)
# @app.route("/oauth2/v1/token", methods=HTTP_METHODS)
@app.route("/test", methods=HTTP_METHODS)
def hello():
    try:
        print(request.headers, file=sys.stdout)
        print(request.data, file=sys.stdout)
        print(request.form, file=sys.stdout)
    except:
        print(request.headers, file=sys.stderr)
        print(request.data, file=sys.stderr)
        print(request.form, file=sys.stderr)
    return "hi"

def alert():
    out = "hey, there! {}".str(datetime.datetime.now())
    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

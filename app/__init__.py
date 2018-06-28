# Flask
from flask import Flask, request
app = Flask(__name__)

# Logging imports
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# Start Log
log_path = "oaflask.log"
handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=1) 
app.logger = logging.getLogger(__name__)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

# Add Routes
from app import routes

# Add Debug Logging
@app.after_request
def after_request(response):
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        app.logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response

# Add Error Logging
@app.errorhandler(Exception)
def exceptions(e):
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    app.logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)

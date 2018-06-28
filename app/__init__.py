from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
app = Flask(__name__)

# Start Log
log_path = "oaflask.log"
logHandler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=1) 
formatter = logging.Formatter('[%(asctime)s] {%(pathname)s - %(levelname)s - %(filename)s - %(module)s - %(funcName)s - %(message)s') 
logHandler.setFormatter(formatter) 
app.logger.addHandler(logHandler) 
app.logger.setLevel(logging.DEBUG)

from app import routes

if __name__ == "__main__":
    app.run(debug=True)


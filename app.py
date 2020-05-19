from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

flaskapp = Flask(__name__)

if __name__ == '__main__':
	logger.debug("Starting the application")
	from api import *  # why does this work only inside

	# host="0.0.0.0"  means it can accept request from any server
	# use_reloader=True  will reload after saving
	flaskapp.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)



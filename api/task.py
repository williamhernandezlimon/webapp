from flask_restful import Resource
import logging as logger

# Task class inherits from Resource class
# Helps us create resource, like http
class Task(Resource):  

	def get(self):
		message = "Inside get method"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code


	# TODO: add relevant methods for post, put, and delete
	def post(self):
		message = "Inside post method"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code

	def put(self):
		message = "Inside put method"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code
	
	def delete(self):
		message = "Inside delete method"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code
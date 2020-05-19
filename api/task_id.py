from flask_restful import Resource
import logging as logger

# Task class inherits from Resource class
# Helps us create resource, like http
class TaskId(Resource):  

	def get(self, task_id):
		message = f"Inside get method of task_id: {task_id}"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code

	def post(self, task_id):
		message = f"Inside post method of task_id: {task_id}"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code

	def put(self, task_id):
		message = f"Inside put method of task_id: {task_id}"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code
	
	def delete(self, task_id):
		message = f"Inside delete method of task_id: {task_id}"
		status_code = 200
		logger.debug(message)
		return {"message": message}, status_code
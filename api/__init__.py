# helps us create new rest server for everything below
from flask_restful import Api

# import our flaskapp
from app import flaskapp

from api.task import Task
from api.task_id import TaskId

# create the resource (path)
rest_server = Api(flaskapp)
rest_server.add_resource(Task, "/api/v1/task")
rest_server.add_resource(TaskId, "/api/v1/task/id/<string:task_id>")
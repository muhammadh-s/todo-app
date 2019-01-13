from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

TODOS = [
    {'task': 'build an API'},
    {'task':  'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod te'},
    {'task': 'profit!'},
    {'task': 'profit!'},
    {'task': 'profit!'},
    {'task': 'profit!'},
]


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# lets you edit and delete an item
class Todo(Resource):
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    # def post(self):
    #     args = parser.parse_args()
    #     todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #     todo_id = 'todo%i' % todo_id
    #     TODOS[todo_id] = {'task': args['task']}
    #     return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/') #GET, POST
api.add_resource(Todo, '/todos/<todo_id>') #DEL, PUT


if __name__ == '__main__':
    app.run(debug=True)
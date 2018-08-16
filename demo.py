from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort, marshal
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 初始化
app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jm_admin:openstack@/39.107.72.235 /jm_db'
# db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True


#定义数据库
# class jm_db(db.Model):
#     __tablename__ = 'all'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     content = db.Column(db.String(80), nullable=False)

list = {
    '1': {'task': 'build an API'},
    '2': {'task': '?????'},
    '3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(id):
    if id not in list:
        abort(404, message="{} doesn't exist".format(id))



# 定义API
class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()
    def get(self, id):
        abort_if_todo_doesnt_exist(id)
        return list[id]

    # def delete(self, id):
    #     abort_if_todo_doesnt_exist(id)
    #     del list[id]
    #     return list[id]+' already deleted', 204
    #
    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('task', type = str)
        super(TaskListAPI, self).__init__()
    def get(self):
        return list

    def post(self):
        parser = reqparse.RequestParser()
        id = int(max(list.keys())) + 1
        args = parser.parse_args()

        list[id] = {'task': args['task']}
        return list[id], 201
        # name = request.json.get('name')
        #
        #
        # db.session.add(name)
        #
        # db.session.commit()
        # return ({'name': name}), 201




api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<id>', endpoint = 'task')

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, jsonify, request
from model import db, Good, Order
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort, marshal

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

api = Api(app, catch_all_404s=True, errors=errors)

# parser = reqparse.RequestParser()
# parser.add_argument('user_name', required=True)
# parser.add_argument('good_num', required=True)
# parser.add_argument('good_id', required=True)

resource_full_fields1 = {
    'id': fields.Integer,
    'good_name': fields.String,
    'good_price': fields.Integer,
    'good_pic_url': fields.String
}


resource_full_fields2 = {
    'user_name': fields.String,
    'num': fields.Integer,
    'good_id': fields.String,
}

resource_full_fields3 = {
    'user_name': fields.String,
    'num': fields.Integer,
    'good_id': fields.String,
    'time': fields.String,
}

class Common:
    def returnTrueJson(self, data, msg="请求成功"):
        return jsonify({
            "status": 1,
            "data": data,
            "msg": msg
        })
    def returnFalseJson(self, data=None, msg="请求失败"):
        return jsonify({
            "status": 0,
            "data": data,
            "msg": msg
        })

class Hello(Resource):
    def get(self):
        return 'Hello Flask!'

# class Users(Resource):
#     # @marshal_with(resource_full_fields, envelope='data')
#     def get(self, userId):
#         user = User.query.filter_by(user_id=userId).first()
#         if (user is None):
#             abort(410, msg="找不到数据", data=None, status=0)
#             # return Common.returnFalseJson(Common)
#         else:
#             return Common.returnTrueJson(Common, marshal(user, resource_full_fields))
#
#     def delete(self, userId):
#         deleteRow = User.query.filter_by(user_id=userId).delete()
#         db.session.commit()
#         if (deleteRow):
#             return UserList.get(UserList)
#         else:
#             return Common.returnFalseJson(Common)
#
#     def put(self, userId):
#         args = parser.parse_args()
#         user_name = args['user_name']
#         user_password = args['user_password']
#         user_nickname = args['user_nickname']
#         user_email = args['user_email']
#         try:
#             user = User.query.filter_by(user_id=userId).first()
#             user.user_name = user_name
#             user.user_password = user_password
#             user.user_nickname = user_nickname
#             user.user_email = user_email
#             db.session.commit()
#             userId = user.user_id
#             data = User.query.filter_by(user_id=userId).first()
#             return Common.returnTrueJson(Common, marshal(data, resource_full_fields))
#         except:
#             db.session.rollback()
#             db.session.flush()
#             abort(409, msg="修改失败", data=None, status=0)
#
#
# class UserList(Resource):
#     # @marshal_with(resource_full_fields, envelope='data')
#     def get(self):
#         # return marshal(User.query.all(), resource_full_fields)
#         return Common.returnTrueJson(Common, marshal(User.query.all(), resource_full_fields))
#
#     def post(self):
#         args = parser.parse_args()
#         user_name = args['user_name']
#         user_password = args['user_password']
#         user_nickname = args['user_nickname']
#         user_email = args['user_email']
#         user = User(user_name=user_name, user_password=user_password, user_nickname=user_nickname,
#                     user_email=user_email)
#         try:
#             db.session.add(user)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             db.session.flush()
#         if (user.user_id is None):
#             return Common.returnFalseJson(Common, msg="添加失败")
#         else:
#             return Users.get(Users, user.user_id)


class GoodList(Resource):
    # @marshal_with(resource_full_fields, envelope='data')
    def get(self):
        # return marshal(User.query.all(), resource_full_fields)
        return Common.returnTrueJson(Common, marshal(Good.query.all(), resource_full_fields1))

    # def post(self):
    #     args = parser.parse_args()
    #     user_name = args['user_name']
    #     user_password = args['user_password']
    #     user_nickname = args['user_nickname']
    #     user_email = args['user_email']
    #     user = User(user_name=user_name, user_password=user_password, user_nickname=user_nickname,
    #                 user_email=user_email)
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
    #     except:
    #         db.session.rollback()
    #         db.session.flush()
    #     if (user.user_id is None):
    #         return Common.returnFalseJson(Common, msg="添加失败")
    #     else:
    #         return Users.get(Users, user.user_id)

# class User(Resource):
#     def get(self, userId):
#             user = User.query.filter_by(user_id=userId).first()
#             if (user is None):
#                 abort(410, msg="找不到数据", data=None, status=0)
#                 # return Common.returnFalseJson(Common)
#             else:
#                 return Common.returnTrueJson(Common, marshal(user, resource_full_fields))
#

parser = reqparse.RequestParser()
parser.add_argument('user_name')
parser.add_argument('num')
parser.add_argument('good_id')

class OrderList(Resource):
    def get(self):
        # return marshal(User.query.all(), resource_full_fields)
        return Common.returnTrueJson(Common, marshal(Order.query.all(), resource_full_fields2))

    def post(self):
        args = parser.parse_args()
        user_name = args['user_name']
        good_id = args['good_id']
        num = args['num']
        order = Order(user_name=user_name, num=num, good_id=good_id)
        try:
            db.session.add(order)
            db.session.commit()
            return Common.returnTrueJson(Common, marshal(Order.query.all()[-1], resource_full_fields2))
        except:
            db.session.rollback()
            db.session.flush()
            return Common.returnFalseJson(Common, msg="添加失败")

class Myorder(Resource):
    def get(self,user_Name):
        myorder = Order.query.filter(Order.user_name==user_Name).all()
        if (myorder is None):
            abort(410, msg="找不到数据", data=None, status=0)
                # return Common.returnFalseJson(Common)
        else:
            return Common.returnTrueJson(Common, marshal(myorder, resource_full_fields3))




# POST格式：curl -d "user_name=123&num=12&good_id=3" "127.0.0.1:5000/orders"

api.add_resource(Hello, '/', '/hello')
# api.add_resource(UserList, '/users')
# api.add_resource(Users, '/users/<int:userId>')
api.add_resource(GoodList, '/goods')
api.add_resource(OrderList, '/orders')
api.add_resource(Myorder, '/orders/<user_Name>')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])


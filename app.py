from flask import Flask, request
from flask_restful import Resource, Api
from db import db


app = Flask(__name__)
api = Api(app)

app.secret_key = 'hose'

db.init_app(app)
items =[]

class Item(Resource):
    def get(self,name):
        item = next(filter(lambda x: x['name'] == name,items), None)
        return {'item':item},200 if item else 404


    def post(self,name):
        if next(filter(lambda x: x['name'] == name,items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json(silent=True)
        items.append(data)
        return {'name':name, 'price': data['price'] },201



class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')


app.run(debug=True)

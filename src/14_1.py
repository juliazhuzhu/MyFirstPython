from xml.etree.ElementTree import parse
from pymongo import *

doc = parse('xml/products.xml')

Client = MongoClient()
db = Client.data
goods = db.goods
'''
for item in doc.iterfind('products/product'):
    id = item.findtext('id')
    name = item.findtext('name')
    price = item.findtext('price')
    print('uuid','=',item.get('uuid'))
    print('id','=',id)
    print('name','=',name)
    print('price','=',price)
    cargo = {}
    cargo["name"] = name
    cargo["id"] = id
    cargo["price"] = price
    cargo_id = goods.insert_one(cargo).inserted_id
'''
for cargo in goods.find():
    print(cargo)

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/loja"
mongo = PyMongo(app)

collection = mongo.db.produto


def ajustar_estoque(sku, estoque) -> None:
    collection.find_one_and_update({'sku': sku}, {"$set": {'estoque': estoque}})


if __name__ == '__main__':
    collection.delete_many({})
    result = collection.insert_one(
        {
            "sku": "U1IT00001",
            "estoque": 340,
        }
    )
    produto = collection.find({'sku': 'U1IT00001'})
    print(f'Antes de atualizar:  {produto[0]}')

    ajustar_estoque(sku='U1IT00001', estoque=512)

    produto = collection.find({'sku': 'U1IT00001'})
    print(f'Após de atualizar:   {produto[0]}')

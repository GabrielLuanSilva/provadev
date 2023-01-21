import pymongo
from flask import Flask
from pymongo.collection import Collection

app = Flask(__name__)


def obter_colecao_mongodb(url_conexao, colecao) -> Collection:
    mongo = pymongo.MongoClient(url_conexao)
    database = mongo["loja"]
    return database[colecao]


if __name__ == '__main__':
    collection = obter_colecao_mongodb(url_conexao="mongodb://localhost:27017/", colecao="produto")
    print(collection)

from flask import Flask
# pymongo lib para crear un cliente para interuactyrar con MongoDB
from pymongo import MongoClient

app = Flask(__name__)

# cliente
client = MongoClient('localhost', 27017)

# db = client.flask_db

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run()

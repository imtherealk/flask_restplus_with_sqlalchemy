from flask import Flask

from api import blueprint
from config import local
from database import db
from serializer import ma

app = Flask(__name__)

app.config.from_object(local)
db.init_app(app)
ma.init_app(ma)
app.register_blueprint(blueprint)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


@app.route('/')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', '8080')

    app.run(host, port)

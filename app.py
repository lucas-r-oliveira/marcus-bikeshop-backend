from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from product.api import create_product_bp

sqlalchemy_engine = create_engine("sqlite:////sqlite.db")
SessionLocal = scoped_session(sessionmaker(bind=sqlalchemy_engine))

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.before_request
def create_session():
    g.db_session = SessionLocal()

@app.before_request
def remove_session():
    g.db_session.close()

app.register_blueprint(create_product_bp(SessionLocal))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

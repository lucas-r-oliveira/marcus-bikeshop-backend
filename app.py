from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, registry

from product.api import create_product_bp

#TODO: review metadata import
from product.orm import start_mappers as map_product, metadata as product_metadata

# Ideally comes from a config
DATABASE_URL = "sqlite:///sqlite.db"
sqlalchemy_engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db(metadata, engine):
    metadata.create_all(bind=engine)

mapper_registry = registry()

map_product(mapper_registry)


init_db(product_metadata, sqlalchemy_engine)
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

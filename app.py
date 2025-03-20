from flask import Flask, g
from flask_pydantic_api import apidocs_views
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, registry

from orders.api import create_orders_bp
from product.api import create_product_bp

from product.orm import start_mappers as map_product
from orders.orm import start_mappers as map_orders

#TODO: review metadata import
from common import metadata

# Ideally comes from a config
DATABASE_URL = "sqlite:///sqlite.db"
sqlalchemy_engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db(metadata, engine):
    metadata.create_all(bind=engine)

mapper_registry = registry()

map_product(mapper_registry)
map_orders(mapper_registry)

init_db(metadata, sqlalchemy_engine)


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
app.register_blueprint(create_orders_bp(SessionLocal))
app.register_blueprint(apidocs_views.blueprint, url_prefix="/apidocs")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

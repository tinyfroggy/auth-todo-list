from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = 'secret_key'

  db.init_app(app)
  Migrate(app, db)

  CORS(app)

  # import the routs
  from routs import register_routes
  register_routes(app, db)

  return app
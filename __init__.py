from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
	app = Flask(__name__)
	app.config["SECRET_KEY"] = "hard to guess string"
	app.debug = True
	db = SQLAlchemy()
	bootstrap = Bootstrap()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False
	bootstrap.init_app(app)
	db.init_app(app)
	return  app
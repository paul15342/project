from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
	app = Flask(__name__)
	db = SQLAlchemy()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False
	db.init_app(app)
	return  app
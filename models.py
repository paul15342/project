
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app

app = create_app()
db = SQLAlchemy(app)

class Info(db.Model):
	__tablename__ = "api_info"
	id = db.Column(db.Integer,primary_key=True)
	address =db.Column(db.String(30))
	agent_id = db.Column(db.String)
	agent_key = db.Column(db.String)
	user_name = db.Column(db.String)
	order_num = db.Column(db.Integer)


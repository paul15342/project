from flask_script import Manager
from __init__ import create_app
from models import db


app = create_app()
manager = Manager(app)


@manager.command
def dev():

    live_sever = Server(app.wsgi_app)
    live_sever.watch('*/*.*')
    live_sever.serve(open_url=True)

@manager.command
def init_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user

db=SQLAlchemy()
DB_Name='Notes.db'


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='My Secret'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_Name}'
    app.config['SQLALCHEMY_DATABASE_URI']='postgres://ngyhtwozmpmeqz:6f83a7f4a752601e9ec07e250a06bfbee185716fff17bc421150c31c76073363@ec2-54-80-122-11.compute-1.amazonaws.com:5432/d8gtv8aqkjjbqa'
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import User,Notes
    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    return app

def create_database(app):
    if not path.exists('website/'+DB_Name):
        db.create_all(app=app)
        print('Created Database!')
from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



db = SQLAlchemy()
DB_NAME = "recipedatabase.db"

def create_app():
    app = Flask(__name__)
    #Initialize bootstrap 
    bootstrap = Bootstrap(app)

    #Keys for the app/database to use 
    app.config['SECRET_KEY'] = 'hUwdBsiekd'
    app.config['SQLALCHEMY_DATABASE_URI'] =f"sqlite:///{DB_NAME}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Recipe

  
    with app.app_context():
        db.create_all()


    return app



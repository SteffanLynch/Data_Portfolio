from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
dbname = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BFHUWOBGSAVFKBNASBFIOEJWFNPQFIKEPRHI'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbname}'

    # say what app we're going to use with the database
    db.init_app(app)

    # we now need to register our blueprints into this app
    # we have to tell we blueprintds that we have external routes and where to find themn

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + dbname):
        # have to tell sqlalchemy which app the database is for
        # Flask-SQLAlchemy 3 no longer accepts an app argument to methods like create_all.
        # Instead, it always requires an active Flask application context.
        with app.app_context():
            db.create_all()
        print("My Guy! You created the database!")

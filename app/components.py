from functools import partial

from flask import Flask
from flask_admin import Admin
import flask_login as login
from flask_sqlalchemy import SQLAlchemy

from app.utils.import_lib import get_setting
from app.admin.utils import load_user

db = SQLAlchemy()


def init_login(app):
    """Init flask login"""
    from app.models import AdminUser
    login_manager = login.LoginManager()
    login_manager.init_app(app)
    login_manager.user_loader(partial(load_user, AdminUser))


def init_admin(app):
    """Init flask admin"""
    from app.admin.views import AdminIndex
    from app.admin.routes import MODEL_VIEWS
    admin = Admin(
        app, index_view=AdminIndex(),
        **app.config['ADMIN_KWARGS']
    )
    for category, views_set in MODEL_VIEWS:
        for model, view in views_set:
            endpoint = '{}_admin'.format(model.__tablename__)
            admin.add_view(view(
                model=model, session=db.session,
                endpoint=endpoint,
                category=category,
            ))


def create_app(settings):
    """Create flask app"""
    app = Flask(
        __name__,
        template_folder=settings.TEMPLATE_FOLDER,
        static_folder=settings.STATIC_FOLDER,
    )

    app.config.from_object(settings)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    # init db
    db.init_app(app)

    # init login
    init_login(app)

    # init admin
    init_admin(app)

    @app.route("/")
    def hello():
        return "Hello World!"
    return app

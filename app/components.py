from functools import partial

from flask import Flask
from flask_admin import Admin
import flask_login as login
from flask_sqlalchemy import SQLAlchemy

from app.utils.import_lib import get_setting
from app.admin.utils import load_user

app = Flask(
    __name__,
    template_folder=get_setting().TEMPLATE_FOLDER,
    static_folder=get_setting().STATIC_FOLDER,
)

app.config.from_object(get_setting())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from app.admin.views import AdminIndex
admin = Admin(
    app, index_view=AdminIndex(), 
    **app.config['ADMIN_KWARGS']
)

from app.models import AdminUser
login_manager = login.LoginManager()
login_manager.init_app(app)
login_manager.user_loader(partial(load_user, AdminUser))


@app.route("/")
def hello():
    return "Hello World!"

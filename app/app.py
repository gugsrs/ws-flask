from flask import Flask
from flask_admin import Admin
import flask_login as login
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)

admin = Admin(app, name='wsTemplate', template_mode='bootstrap3')

login_manager = login.LoginManager()
login_manager.init_app(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

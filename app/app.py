from flask import Flask
from flask_admin import Admin
import flask_login as login


app = Flask(__name__)

admin = Admin(app, name='wsTemplate', template_mode='bootstrap3')
login_manager = login.LoginManager()
login_manager.init_app(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

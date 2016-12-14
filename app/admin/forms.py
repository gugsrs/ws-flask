from werkzeug.security import check_password_hash
from wtforms import form, fields, validators

from app.models import AdminUser


class Login(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, _):
        self.user = self.get_user()
        if self.user is None:
            raise validators.ValidationError('Invalid User')
        
    def validate_password(self, _):
        if self.user is not None:
            self.authenticate()

    def get_user(self):
        return AdminUser.query.filter_by(email=self.login.data).first()

    def authenticate(self):
        if not check_password_hash(self.user.password, self.password.data):
            raise validators.ValidationError('Invalid Password')


class AdminUserForm(form.Form):
    email = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField()
    password_verification = fields.PasswordField()

    def validate_password(self, _):
        if self.password.data != self.password_verification.data:
            raise validators.ValidationError('Password doesn\'t match')

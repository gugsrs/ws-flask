import flask_admin as admin
import flask_login as login

from flask import request, render_template
from wtforms import validators
from werkzeug.security import generate_password_hash

from app.admin import forms, utils
from app.utils.views import redirect_to
from app import models


class AdminIndex(admin.AdminIndexView):
    """Flask-admin blueprint to handle authentication on flask-login"""

    @admin.expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect_to('.login')
        return super(AdminIndex, self).index()

    @admin.expose('/login/', methods=('GET', 'POST'))
    def login(self):
        """Controller for authentication on flask-login"""
        form = forms.Login(request.form)
        if admin.helpers.validate_form_on_submit(form):
            login.login_user(form.user)
        if login.current_user.is_authenticated:
            return redirect_to('.index')
        self._template_args['form'] = form
        return super(AdminIndex, self).index()

    @admin.expose('/logout/')
    def logout(self):
        """Controller for login out from flask-login."""
        login.logout_user()
        return redirect_to('.index')


class AdminUser(utils.BaseModelView):
    """Custom flask-admin blueprint for AdminUser"""
    column_sortable_list = ['email']
    column_list = ['email']
    form = forms.AdminUserForm
        
    def create_model(self, form):
        """Customisation of flask-admin create_model for AdminUser."""
        form.password.data = generate_password_hash(form.password.data)
        return super(AdminUser, self).create_model(form)

    def update_model(self, form, obj):
        form.password.data = generate_password_hash(form.password.data)
        return super(AdminUser, self).updateform(form, obj)

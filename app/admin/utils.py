import flask_login as login
import json
import logging

from flask import render_template as render
from flask_admin.contrib import sqla
from wtforms import validators

from app.utils import import_lib


def json_validator(form, field):
    """"""
    try:
        json.loads(field.data)
    except ValueError as e:
        raise validators.ValidationError(str(e))


def render_template(template_name, **kwargs):
    settings = import_lib.get_settings()
    return render(
        '/'.join((settings.ADMIN_TEMPLATES, template_name)),
        **kwargs
    )


def load_user(user_model, user_id):
    return user_model.query.get(int(user_id))


class BaseModelView(sqla.ModelView):
    column_default_sort = ('id', True)

    def is_accessible(self):
        return login.current_user.is_authenticated()

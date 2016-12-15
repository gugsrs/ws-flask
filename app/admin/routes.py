from app import models
from app.admin import utils, views


MODEL_VIEWS = (
    (
        'AdminUser', (
            (models.AdminUser, views.AdminUser),
        ),
    ),
)

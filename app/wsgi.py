from .components import create_app
from app.utils.import_lib import get_setting


application = create_app(get_setting())

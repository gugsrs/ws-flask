"""Functions to import classes."""
import os
from app import settings


def get_setting(settings_name=None):
    """Shortcut to loading settings class by name."""
    settings_name = settings_name or os.getenv('SETTINGS', 'Development')
    return getattr(settings, settings_name)

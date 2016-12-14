from flask import redirect, url_for
from app.utils.import_lib import get_setting

setting=get_setting()


def redirect_to(name=None, url=None, code=setting.REDIRECT_CODE, **kwargs):
    if name is None:
        if url is None:
            raise ValueError('one of name or url is required')
        return redirect(url, code=code)
    return redirect(url_for(name, **kwargs), code=code)

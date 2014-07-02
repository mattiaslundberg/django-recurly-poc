import recurly
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

recurly.SUBDOMAIN = settings.SUBDOMAIN
recurly.API_KEY = settings.RECURLY_API
recurly.js.PRIVATE_KEY = settings.RECURLY_PUBLIC

class LoginRequired(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)

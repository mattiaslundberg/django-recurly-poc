import recurly
from django.conf import settings

recurly.SUBDOMAIN = settings.SUBDOMAIN
recurly.API_KEY = settings.RECURLY_API
recurly.js.PRIVATE_KEY = settings.RECURLY_PUBLIC

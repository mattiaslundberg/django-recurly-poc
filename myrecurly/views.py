from django.views.generic.base import TemplateView
from myrecurly.utils import LoginRequired

class HomeView(LoginRequired, TemplateView):
    template_name = "home.html"

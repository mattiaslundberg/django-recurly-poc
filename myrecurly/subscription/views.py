from django.views.generic.base import TemplateView
from rest_framework import views
from django.http import HttpResponse

class SubscriptionView(TemplateView):
    template_name = "subscription_main.html"

class BillingInfo(views.APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("sometext")

    def set(self, request, *args, **kwargs):
        pass

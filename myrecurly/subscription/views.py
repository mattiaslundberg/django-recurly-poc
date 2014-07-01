from django.views.generic.base import TemplateView
from rest_framework import views
from django.http import HttpResponse
from myrecurly.utils import recurly
from django.conf import settings

class SubscriptionView(TemplateView):
    template_name = "subscription_main.html"

    def get_context_data(self, **kwargs):
        context = super(SubscriptionView, self).get_context_data(**kwargs)
        context["RECURLY_PUBLIC"] = settings.RECURLY_PUBLIC
        return context

class BillingInfo(views.APIView):
    def get(self, request, *args, **kwargs):
        recurly_account = recurly.Account.get(request.user.id)
        try:
            return HttpResponse(recurly_account.billing_info)
        except:
            return HttpResponse()

    def post(self, request, *args, **kwargs):
        recurly_account = recurly.Account.get(request.user.id)
        recurly_account.billing_info = recurly.BillingInfo(token_id=request.POST["recurly-token"])
        recurly_account.save()
        return HttpResponse()

class SubscriptionInfo(views.APIView):
    def get(self, request, *args, **kwargs):
        recurly_account = recurly.Account.get(request.user.id)
        return HttpResponse(recurly_account.subscriptions()[0].state)

    def post(self, request, *args, **kwargs):
        recurly_account = recurly.Account.get(request.user.id)
        subscription = recurly.Subscription(plan_code="haxxor", currency="EUR", account=recurly_account)
        subscription.save()
        return HttpResponse("Saved")

    def delete(self, request, *args, **kwargs):
        recurly_account = recurly.Account.get(request.user.id)
        recurly_account.subscripsions().cancel()
        return HttpResponse()

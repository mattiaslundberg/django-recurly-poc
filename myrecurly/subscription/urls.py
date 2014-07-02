from django.conf.urls import patterns, url
from myrecurly.subscription.views import SubscriptionView

urlpatterns = patterns("",
        url(r"^$", SubscriptionView.as_view(), name="subscription"),
    )

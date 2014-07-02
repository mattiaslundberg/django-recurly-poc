from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from myrecurly.subscription.views import BillingInfo, SubscriptionInfo
from myrecurly.views import HomeView

urlpatterns = patterns("",
    url(r'^$', HomeView.as_view(), name='home'),

    url(r"^api/billing/", BillingInfo.as_view()),
    url(r"^api/subscription/", SubscriptionInfo.as_view()),

    url(r"^subscription/", include("myrecurly.subscription.urls")),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^accounts/", include("registration.backends.simple.urls")),
)

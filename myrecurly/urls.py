from django.conf.urls import patterns, include, url
from django.conf.urls.default import login_required
from django.contrib import admin
admin.autodiscover()

from myrecurly.subscription.views import BillingInfo

urlpatterns = patterns("",
    # Examples:
     url(r'^$', 'recurly.views.home', name='home'),

     url(r"^api/billing/$", login_required(BillingInfo.as_view())),
    # url(r'^blog/', include('blog.urls')),

    url(r"^subscription/", include("myrecurly.subscription.urls")),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^accounts/", include("registration.backends.default.urls")),
)

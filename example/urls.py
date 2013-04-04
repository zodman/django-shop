from django.conf.urls.defaults import *
from .myshop.views import MyOrderConfirmView
from shop_simplevariations import urls as simplevariations_urls
from shop import urls as shop_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
   (r'^cart/', include(simplevariations_urls)),

    (r'^', include(shop_urls)), # <-- That's the important bit


)

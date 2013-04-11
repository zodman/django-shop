<<<<<<< HEAD
from django.conf.urls.defaults import *
from .myshop.views import MyOrderConfirmView, products_view
from shop_simplevariations import urls as simplevariations_urls
=======
from django.conf.urls import patterns, include, url
from example.myshop.views import MyOrderConfirmView

>>>>>>> 7675ef4ca59336c42c117aab6a713f651f9c3458
from shop import urls as shop_urls
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
   (r'^cart/', include(simplevariations_urls)),
    (r'^products/',products_view),
   url(r'^', include('filer.server.urls')),
    (r'^', include(shop_urls)), 


)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, 
	 	document_root=settings.MEDIA_ROOT)


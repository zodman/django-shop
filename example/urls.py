from django.conf.urls.defaults import *
from .myshop.views import MyOrderConfirmView, products_view
from shop_simplevariations import urls as simplevariations_urls
from example.myshop.views import MyOrderConfirmView
from shop import urls as shop_urls
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from example.myshop.views import welcome_view, category_view
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
   (r'^cart/', include(simplevariations_urls)),
  #  (r'^products/',products_view),
    url(r'^products/category/(?P<slug>[a-zA-z0-9\-]+)',category_view, name="category_detail"),
    url(r"^$",welcome_view, name="welcome"),
   url(r'^', include('filer.server.urls')),
    (r'^', include(shop_urls)), 


)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, 
	 	document_root=settings.MEDIA_ROOT)


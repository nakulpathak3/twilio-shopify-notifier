from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'shopify_app.views.home', name='home'),
    url(r'login/', include('shopify_auth.urls')),
    url(r'order_webhook/', 'shopify_app.views.webhook', name='webhook'),
    url(r'^twilio_call/(?P<product_name>[a-zA-Z-]+)/$', 'shopify_app.views.twilio_call', name='twilio_call'),
]

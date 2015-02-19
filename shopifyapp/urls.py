from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'shopify_app.views.home', name='home'),
    url(r'login/', include('shopify_auth.urls')),
]

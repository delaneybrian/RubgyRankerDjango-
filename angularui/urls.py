from django.conf.urls import url
from angularui import views

urlpatterns = [
    #SPA URL
    url(r'', views.index),
]


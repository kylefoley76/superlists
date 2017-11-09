# from django.conf.urls import *
# from django.contrib import admin

# from django.contrib.auth.views import login
# from lists import views as myapp_views


from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]
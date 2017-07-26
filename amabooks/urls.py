from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r"^register/$", views.register, name = "register"),
        url(r"^login/$", views.login, name = "login"),
        url(r"^upload/$", views.upload, name = "upload"),
        url(r"^order_book/$", views.order_book, name = "order"),

]

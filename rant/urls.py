from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('rule', views.rule, name="rule"),
    path('login', views.login, name="login"),

]
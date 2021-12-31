from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path("display/", views.index),
    path("display/add/", views.add_page),
    path("display/add/push/", views.add_team_member),
]


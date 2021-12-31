from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path("display/", views.display_page),
    path("display/add/", views.add_page),
    path("display/add/push/", views.add_team_member),
    path("display/edit/", views.edit_page),
]


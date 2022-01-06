from django.urls import path
from . import views


urlpatterns = [
    path("", views.MemberList.as_view(), name="display"),
    path("add/", views.add_page, name="add"),
    path("edit/", views.edit_page, name="edit"),
]


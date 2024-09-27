from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:project_id>/", views.detail, name="detail"),
    path("<int:project_id>/results", views.results, name="results"),
    path("<int:project_id>/edit/", views.edit, name="edit"),
]

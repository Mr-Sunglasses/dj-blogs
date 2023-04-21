from django.urls import path
from posts import views
urlpatterns = [
    path("new_post", views.new, name="new_post"),
    path("<int:id>", views.details, name="details"),
    path("delete/<int:id>", views.delete, name="delete"),
]
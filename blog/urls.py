from django.urls import path
from blog import views
urlpatterns = [
    path("", views.welcome, name="welcome"),
    # path("welcome/", views.welcome, name="welcome")
]
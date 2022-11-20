from django.urls import path

from . import views

urlpatterns = [
    path("object/", views.category_view, name="objects"),
]

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
   path("", views.index, name="index"),  # herhangi bir yol yoksa indexe gitsin anlamındadır



]
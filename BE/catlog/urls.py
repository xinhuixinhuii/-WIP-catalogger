from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:catLogName>/", views.detail, name="detail"),
    path("<str:catLogName>/result/", views.result, name="result")
]
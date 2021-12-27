from django.urls import path
from . import views

urlpatterns = [
    path('alphabets/', views.write_alphabets)
]
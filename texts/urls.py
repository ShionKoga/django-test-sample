from django.urls import path
from . import views

app_name = 'texts'

urlpatterns = [
    path('alphabets/', views.write_alphabets, name='alphabets')
]
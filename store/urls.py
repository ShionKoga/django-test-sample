from django.urls import path
from . import views

urlpatterns = [
    path('meats/', views.buy_meats)
]
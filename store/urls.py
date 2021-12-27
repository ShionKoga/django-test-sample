from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('meats/', views.buy_meats, name = 'meats')
]
from django.urls import path
from .views import show_exchange_rates

urlpatterns = [
    path('show_rates/', show_exchange_rates,),
]
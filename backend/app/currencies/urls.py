from django.urls import path

from .views import CurrencyCreateView, CurrencyDetailView


app_name = 'currencies'

urlpatterns = [
    path('<int:pk>/', CurrencyDetailView.as_view()),
    path('', CurrencyCreateView.as_view()), 
]
    
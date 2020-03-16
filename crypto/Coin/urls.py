from django.urls import path
from .views import Home

app_name = 'Coin'

urlpatterns = [
    path('', Home, name='home')
]

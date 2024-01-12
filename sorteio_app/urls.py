from django.urls import path
from .views import sorteio, login

urlpatterns = [
    path('sorteio/', sorteio, name='sorteio'),
    path('login/', login, name='login'),
]

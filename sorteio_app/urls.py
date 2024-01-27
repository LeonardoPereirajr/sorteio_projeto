from django.urls import path
from .views import sorteio, login
from . import views

urlpatterns = [
    path('sorteio/', sorteio, name='sorteio'),
    path('login/', login, name='login'),
    path('sorteio_upload/', views.sorteio_upload, name='sorteio_upload'),
]

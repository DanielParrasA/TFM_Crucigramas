from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('obtener_palabra/<int:letras>/', views.obtener_palabra, name='obtener_palabra'),
    path('obtener_pista/<str:palabra_obtenida>/', views.obtener_pista, name='obtener_pista')
]
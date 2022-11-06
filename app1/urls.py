from django.urls import path
from app1.views import mostrar_familiares


urlpatterns = [
    path('familiares/', mostrar_familiares)
]
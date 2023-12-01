from django.urls import path
from usuarios.views import UsuarioRegistroView


urlpatterns = [
   path('registro/',UsuarioRegistroView.as_view(),name='Registro'),
   

]


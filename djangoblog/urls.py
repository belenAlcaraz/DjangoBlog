"""
URL configuration for djangoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    ------- Anotaciones propias: -------
    ' ':la cadena vacia representa la ruta principal de la app
    InicioView.as_view(): asocia la vista InicioViewcon dicha URL.
    as_view()  se utiliza con vistas basadas en clases para convertirlas 
    en funciones de vista que pueden ser utilizadas en el sistema de enrutamiento de URLs de Django.

    Las vistas basadas en clases son clases de py q heredan de una de las clases de vistas q genera 
    django como por ejemplo ListView(se esta utilizando)

    Explicacion de <int:pk> : pk es la primaryKey,y es la pk de cada entrada del blog,cada vez que se crea 
    una entrada al ingresar a un nuevo blog, se le asigna un numero de identificacion unico
    django genera eso,junto con la base de datos
    entonces cada blog tiene su pk: la 1ra publicacion es articulo/1

"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path
from blog.views import InicioView, ArticuloView, AgregarPostView, ActualizarPostView, EliminarPostView, ComentarioPostView, EliminarComentarioView, ActualizarComentarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name= "Inicio",),
    path('articulo/<int:pk>', ArticuloView.as_view(), name='Articulos'),
    path('agregar_publicacion/', AgregarPostView.as_view(),name='Agregar_publicacion'),
    path('articulo/actualizar/<int:pk>', ActualizarPostView.as_view(), name= 'Actualizar_publicacion'),
    path('articulo/eliminar_publicacion/<int:pk>', EliminarPostView.as_view(), name='Eliminar_publicacion'),
    path('articulo/agregar_comentario/<int:publicacion_id>/', ComentarioPostView.as_view(), name='Agregar_comentario'),
    path('articulo/eliminar_comentario/<int:pk>', EliminarComentarioView.as_view(), name='Eliminar_comentario'),
    path('articulo/actualizar_comentario/<int:pk>', ActualizarComentarioView.as_view(), name='Actualizar_comentario'),
    #Apartir de  aquí uso la url de la app usuarios
    path('usuarios/',include('django.contrib.auth.urls')),
    path('usuario/',include('usuarios.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
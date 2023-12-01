from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import PermissionDenied
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publicacion, Comentario, Categoria
from .forms import PostForm, ActualizarForm, ComentarioForm, ActualizarComentarioForm

#################### Publicación ####################

class InicioView(ListView):
    model = Publicacion  # Significa que trabaja con el model publicacion
    template_name = 'index.html' # mientras que template indica la planilla que se utiliza para mostrar la lista de obj
    ordering = ['-creacion']
    
    """ Seguramente se borra
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categorias__id = categoria_id) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categorias'] = Categoria.objects.all()
        return context
    """ 
    
class ArticuloView(DetailView):
    model = Publicacion
    template_name = 'articulos.html'  # indica la platilla que muetra los detalles de los objetoss

    def get_context_data(self,**kwargs):
        """
        Esto agrega informacion adicional al contexto de la vista.
        """
        context = super().get_context_data(**kwargs)
        context['es_autor'] = self.request.user == self.get_object().autor
        return context
    
class AgregarPostView(CreateView):
    model = Publicacion
    form_class = PostForm
    template_name = 'agregar_post.html'    # fields = '__all__' #esto "trae" todos los campos
    success_url = reverse_lazy('Inicio')
    
class ActualizarPostView(UpdateView):
    model = Publicacion
    form_class = ActualizarForm
    template_name = 'actualizar_post.html' #fields = ["titulo", "cuerpo"] no son necesario los fields al usar el form_class

class EliminarPostView(DeleteView):
    model = Publicacion
    template_name = 'eliminar_post.html' 
    success_url = reverse_lazy('Inicio')

#################### Comentario ####################

class ComentarioPostView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'agregar_comentario.html'
    success_url = reverse_lazy('Articulos')

    def get_success_url(self):
        """
         Retorna la URL de redirección a la vista 'Articulos' con el pk de la publicación asociada al comentario.
        """
        publicacion_pk = self.kwargs['publicacion_id']
        return reverse_lazy('Articulos', kwargs={'pk': publicacion_pk})
    
    def form_valid(self, form):

        """
        Procesa y guarda un comentario, asignándole la publicación que le correspondiente.

        Parámetros:
        - self: Instancia de la vista basada en clase.
        - form: Formulario validado con los datos del comentario.

        Retorna:
        - Guarda la instancia en la base de datos.

        """ 
        publicacion = get_object_or_404(Publicacion, pk=self.kwargs['publicacion_id'])
        form.instance.publicacion = publicacion
        return super().form_valid(form)
    
class EliminarComentarioView(DeleteView):
    model = Comentario 
    template_name = 'eliminar_comentario.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        comentario_pk = self.kwargs['pk']
        return get_object_or_404(Comentario, pk=comentario_pk)
    

class ActualizarComentarioView(UpdateView):
    model = Comentario
    form_class = ActualizarComentarioForm
    template_name = 'actualizar_comentario.html' 

    
    def dispatch(self,request,*args,**kwargs):
        comentario = self.get_object() # --> es un método proporcionado por la clase base DetailView
        print(f"Comentario autor: {comentario.autor}, Usuario: {request.user}")
        if request.user != comentario.autor:
            raise PermissionDenied("No tienes permiso para actualizar este comentario.") 
            #--> Esta excepción se utiliza para indicar que un usuario no tiene permisos suficientes para realizar una acción
        return super().dispatch(request,*args,**kwargs)
    
        """
        request se utiliza para obtener información sobre el usuario que está realizando la solicitud, 
        y request.user proporciona el objeto de usuario asociado con la solicitud 
        """
    
    def get_success_url(self):
        """
        Retorna la URL de redirección a la vista 'Articulos' con el pk de la publicación asociada al comentario.
        
        """
        publicacion_pk = self.get_object().publicacion.pk
        return reverse_lazy('Articulos', kwargs={'pk': publicacion_pk})
    

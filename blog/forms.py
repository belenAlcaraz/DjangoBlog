from django import forms
from .models import Publicacion, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ("autor", "titulo", "cuerpo", "categorias")

        widgets = {
            "autor": forms.Select(attrs={'class': 'form-control'}),
            "titulo": forms.TextInput(attrs={'class': 'form-control'}),
            "cuerpo": forms.Textarea(attrs={'class': 'form-control'}),
            "categorias": forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

class ActualizarForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ("autor", "titulo", "cuerpo")
        widgets = {
            "autor": forms.Select(attrs={'class': 'form-control'}),
            "titulo": forms.TextInput(attrs={'class': 'form-control'}),
            "cuerpo": forms.Textarea(attrs={'class': 'form-control'}),            
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor','cuerpo')
        widgets = {
            "autor": forms.Select(attrs={'class': 'form-control'}),
            "cuerpo": forms.Textarea(attrs={'class': 'form-control'}),            
        }


class ActualizarComentarioForm(forms.ModelForm): 
    class Meta:
        model = Comentario
        fields = ('cuerpo',)
        widgets = {
            "cuerpo": forms.Textarea(attrs={'class': 'form-control'}),            
        }

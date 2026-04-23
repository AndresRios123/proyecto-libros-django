from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
from django import forms
from .models import Tesis

class TesisForm(forms.ModelForm):
    class Meta:
        model = Tesis
        # Definimos qué campos vamos a permitir editar manualmente
        fields = [
            'titulo', 
            'autor_name', 
            'director', 
            'codirector', 
            'program', 
            'publication_year', 
            'abstract', 
            'pdf_file'
        ]
        
        # Aquí inyectamos Tailwind CSS a cada input
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-blue-500 focus:border-blue-500'}),
            'autor_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1'}),
            'director': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1'}),
            'codirector': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1'}),
            'program': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 bg-white'}),
            'publication_year': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1'}),
            'abstract': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1', 'rows': 4}),
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1'}),
        }
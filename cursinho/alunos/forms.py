from django import forms

from .models import RegisterAluno

class RegisterAlunoForm(forms.Form):
    
    class Meta:
        model = RegisterAluno()
        fields = ['nome', 'email', 'sex', 'dCronicas', 'estcivil',
            'qtdfilhos', 'concEnsMed', 'bolsaEnsMed']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome',
                'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email',
                'class': 'form-control',}),
            'sex': forms.TextInput(attrs={'placeholder': 'Sexo',
                'class': 'form-control',}),
            'dCronicas': forms.TextInput(attrs={'placeholder': 'Doenças Crônicas',
                'class': 'form-control',}),
            'estcivil': forms.TextInput(attrs={'placeholder': 'Estado Civil',
                'class': 'form-control',}),
            'qtdfilhos': forms.TextInput(attrs={'placeholder': 'Quantidade de Filhos',
                'class': 'form-control',}),
            'concEnsMed': forms.TextInput(attrs={'placeholder': 'Conclusão do Ensino Médio',
                'class': 'form-control',}),
            'bolsaEnsMed': forms.TextInput(attrs={'placeholder': 'Bolsa no Ensino Médio',
                'class': 'form-control',}),
        }

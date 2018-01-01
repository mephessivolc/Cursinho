from django import forms
from django.db import transaction

from .models import RegisterEnd, RegisterContact

from cursinho.accounts.models import User


class RegisterEndForm(forms.ModelForm):

    def save(self, commit=True):
        end = super(RegisterEndForm, self).save(commit=False)

        if idRef['idAluno'] is not None:
            dbAluno = RegisterAluno.objects.get(id = idRef['idAluno'])
            end.idPupil = dbAluno

        elif idRef['idUser'] is not None:
            dbUser = User.objects.get(id = idRef['idUser'])
            end.idUser = dbUser

        if commit:
            end.save()

        return end.pk

    class Meta:
        model = RegisterEnd
        fields = ['end', 'numero', 'cep', 'bairro', 'comp']

        widgets = {
            'end': forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control',}),
            'numero': forms.TextInput(attrs={'placeholder': 'Numero', 'class': 'form-control',}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro', 'class': 'form-control',}),
            'comp': forms.TextInput(attrs={'placeholder': 'Complemento', 'class': 'form-control',}),
            'cep': forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control',}),
        }

class RegisterContactForm(forms.ModelForm):

    def save(self, commit=True):
        contact = super(RegisterContactForm, self).save(commit=False)

        # if idAluno is not None:
        #     dbAluno = RegisterAluno.objects.get(id = idAluno)
        #     contact.idPupil = dbAluno

        if commit:
            contact.save()

        return contact.pk

    class Meta:
        model = RegisterContact
        fields = ['tel', 'cel', 'email',]

        widgets = {
            'tel': forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control',}),
            'cel': forms.TextInput(attrs={'placeholder': 'Celular', 'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control',}),

        }

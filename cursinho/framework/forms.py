from django import formss

class RegisterEndForm(forms.ModelForm):

    class Meta:
        model = RegisterEnd
        fields = ['end', 'numero', 'cep', 'bairro', 'comp', 'idUser']

        widgets = {
            'end': forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control',}),
            'numero': forms.TextInput(attrs={'placeholder': 'Numero', 'class': 'form-control',}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro', 'class': 'form-control',}),
            'comp': forms.TextInput(attrs={'placeholder': 'Complemento', 'class': 'form-control',}),
            'cep': forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control',}),
            'idUser': forms.HiddenInput(),
        }

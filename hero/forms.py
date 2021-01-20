from django import forms

class RegistrationForm(forms.Form):
    razao_social = forms.CharField(max_length=50)
    nome_fantasia = forms.CharField(max_length=50)
    telefone_comercial = forms.CharField(max_length=50)
    inscricao_municipal_Estadual: forms.CharField(max_length=50)
    cnpj = forms.CharField(max_length=40)
    endereco = forms.CharField(max_length=150)
    email = forms.CharField(max_length=50)

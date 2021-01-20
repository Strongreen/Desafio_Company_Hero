from django.db import models


class Company(models.Model):
    razao_social = models.CharField(max_length=50)
    nome_fantasia = models.CharField(max_length=50)
    telefone_comercial = models.CharField(max_length=50)
    inscricao_municipal_estadual = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=40)
    endereco = models.CharField(max_length=150)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.razao_social


class Employeer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name

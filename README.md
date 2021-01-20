# Desafio Company Hero
Desafio processo seletivo da Company Hero
Desenvolvedor Python Jr.
Criação de uma API em Django Rest Framework


# Descrição de como utilizar a API.

Obs: A descrição foi baseada para configurar via postman


## Company

### GET de todas as empresas
```
http://127.0.0.1:8000/company/
```

### GET de uma empresa específica com os funcionarios que trabalham nessa empresa

**Params: cnpj**

```
http://127.0.0.1:8000/company/:cnpj
```

### POST 

```
http://127.0.0.1:8000/company/
```

**Body**:
```
{
    "razao_social": "Razão social da empresa",
    "nome_fantasia": "nome fantasia da empresa",
    "telefone_comercial": "telefone da empresa",
    "cnpj": "CNPJ da empresa",
    "endereco": "Endereço completo comercial da empresa",
    "email": "email da empresa"
}
```


## Employeer

### GET de todas os funcionarios
```
http://127.0.0.1:8000/employeer/
```

### GET de uma funcionarios específico com as empresas que ele trabalha

**Params: username**

```
http://127.0.0.1:8000/employeer/:username
```

### POST 

```
http://127.0.0.1:8000/employeer/:username
```

**Body**:
```
{
    "name": "nome do funcionario",
    "username": "user name do funcionario",
    "cargo": "cargo do funcionario",
    "cpf": "cpf do funcionario",
    "company": "id da company - este campo deve ser um int"
}
```

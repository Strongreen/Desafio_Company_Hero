# Desafio Company Hero
#### Desafio processo seletivo da Company Hero
#### Desenvolvedor Python Jr.
#### Criação de uma API em Django Rest Framework


# Descrição de como utilizar a API. </h3>

Obs: A descrição foi baseada para configurar via postman


## Company

### GET de todas as empresas
```
https://desafiocompanyhero.herokuapp.com/company/
```

```
Exemplo do response do GET:
[
    {
        "id": 1,
        "razao_social": "Company Hero",
        "nome_fantasia": "Company Hero",
        "telefone_comercial": "11 2233 4422",
        "inscricao_municipal_estadual": "123456789",
        "cnpj": "20240272000176",
        "endereco": "Rua da sede",
        "email": "people@companyhero.com"
    }
]

```


### GET de uma empresa específica com os funcionários que trabalham nessa empresa

**Params: cnpj**

```
https://desafiocompanyhero.herokuapp.com/company/:cnpj
```

```
Exemplo do response do GET passando o parametro cnpj:
{
    "razao_social": "Company Hero",
    "nome_fantasia": "Company Hero",
    "telefone_comercial": "11 2233 4422",
    "inscricao_municipal_estadual": "123456789",
    "cnpj": "20240272000176",
    "endereco": "Rua da sede",
    "email": "people@companyhero.com",
    "employeers": [
        "Hérika"
    ]
}

```

```
Caso a API não encontre nenhuma empresa com o CNPJ:
{
    "error": "Empresa não encontrado!"
}

```



### POST 

```
https://desafiocompanyhero.herokuapp.com/company/

Header
Content-Type: application/json

```

**Body**:
```
{
    "razao_social": "Razão social da empresa",
    "nome_fantasia": "nome fantasia da empresa",
    "telefone_comercial": "telefone da empresa",
    "inscricao_municipal_estadual": "incricao municipal ou inscricao estadual",
    "cnpj": "CNPJ da empresa",
    "endereco": "Endereço completo comercial da empresa",
    "email": "email da empresa"
}
```


```
Especificação dos campos:
{
    "razao_social": string,
    "nome_fantasia": string,
    "telefone_comercial": string,
    "inscricao_municipal_estadual": string,
    "cnpj": string,
    "endereco": string,
    "email": string
}
```

## Employeer

### GET de todos os funcionários
```
https://desafiocompanyhero.herokuapp.com/employeer/
```
```
Exemplo do response do GET:
[
    {
        "id": 1,
        "name": "Hérika",
        "username": "strongreen",
        "cargo": "dev python jr",
        "cpf": "0803030040",
        "company": 1
    }
]
```




### GET de um funcionário específico com as empresas que ele trabalha

**Params: username**

```
https://desafiocompanyhero.herokuapp.com/employeer/:username
```

```
Exemplo do response do GET passando como parametro o username:
{
    "name": "Hérika",
    "cpf": "0803030040",
    "cargo": "dev python jr",
    "username": "strongreen",
    "companies": [
        "Company Hero"
    ]
}
```

```
Caso a API não encontre nenhum funcionário com parametro username informado:
{
    "error": "Funcionario não encontrado!"
}
```

### POST 

```
https://desafiocompanyhero.herokuapp.com/employeer/
Header
Content-Type: application/json
```

**Body**:
```
{
    "name": "nome do funcionario",
    "username": "user name do funcionario",
    "cargo": "cargo do funcionario",
    "cpf": "cpf do funcionario",
    "company": "id da company"
}
```

```
Especificação dos campos:
{
    "name": string,
    "username": string,
    "cargo": string,
    "cpf": string,
    "company": int
}
```


## Stacks utilizadas no projeto
- Python 3.8.7
- Django 3.1.5
- Django Rest Framework
- Postgres
- Heroku

### Diagrama da estrutura do BD

 ![](https://github.com/Strongreen/Desafio_Company_Hero/blob/main/diagrama.png)

### Método de organização e planejamento utilizado para realizar o desafio

**Trello**
https://trello.com/invite/b/C4tMnmN2/9de9dc86b0e1e9287be67310a676ce80/company-hero-python

#### Link da proposta

https://www.notion.so/Teste-Python-Company-Hero-210200be44044560b450d6e80e27431b

# Desafio Company Hero
#### Desafio processo seletivo da Company Hero
#### Desenvolvedor Python Jr.
#### Criação de uma API em Django Rest Framework


# Descrição de como utilizar a API. </h3>

Obs: A descrição foi baseada para configurar via postman


## Company

### GET de todas as empresas
```
http://127.0.0.1:8000/company/
```

### GET de uma empresa específica com os funcionários que trabalham nessa empresa

**Params: cnpj**

```
http://127.0.0.1:8000/company/:cnpj
```

### POST 

```
http://127.0.0.1:8000/company/

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
http://127.0.0.1:8000/employeer/
```

### GET de um funcionário específico com as empresas que ele trabalha

**Params: username**

```
http://127.0.0.1:8000/employeer/:username
```

### POST 

```
http://127.0.0.1:8000/employeer/:username
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
- Python 3.8.5
- Django 3.1.5
- Django Rest Framework
- Postgres

### Diagrama da estrutura do BD

 ![](https://github.com/Strongreen/Desafio_Company_Hero/blob/main/diagrama.png)



#### Link da proposta

https://www.notion.so/Teste-Python-Company-Hero-210200be44044560b450d6e80e27431b

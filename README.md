# django_api_rest

Este repositório é um exemplo básico de como implementar operações CRUD (Create, Read, Update, Delete) usando o Django REST Framework (DRF). O projeto inclui um modelo `Cadastro` com campos para nome, idade e data de cadastro, além de views e serializers para manipular esses dados via API.

## Funcionalidades

- **Cadastro de Pessoas**: Crie, leia, atualize e delete registros de pessoas.
- **API RESTful**: Endpoints para todas as operações CRUD.
- **Respostas Formatadas**: Respostas JSON bem estruturadas para facilitar o consumo da API.

## Tecnologias Utilizadas

- **Django**: Framework web Python.
- **Django REST Framework**: Framework para construção de APIs RESTful em Django.
- **SQLite**: Banco de dados padrão para desenvolvimento.

## Estrutura do Projeto

- **`core/`**: Configurações principais do projeto Django.
- **`app/`**: Aplicação Django que contém o modelo `Cadastro`, views e serializers.


## Como Executar o Projeto

1. **Clone o repositório**:
```bash
    git clone https://github.com/moscarde/django_api_rest.git
    cd django_api_rest
```

2. **Crie um Ambiente Virtual e Instale as Dependências**:
```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

3. **Execute as Migrações**:
```bash
    python manage.py migrate
```

4. **Inicie o Servidor de Desenvolvimento**:
```bash
    python manage.py runserver
```

5. **Acesse a API**:

`DEBUG_MODE = True`
- **Listagem e Cadastro de Pessoas**: `http://localhost:8000/` (método GET e POST)
- **Busca, Atualiza e Deleta de Pessoas**: `http://localhost:8000/<id>` (método GET, PUT e DELETE)

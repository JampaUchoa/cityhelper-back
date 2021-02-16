Serviço REST Principal para o cidadão consultar / visualizar / filtrar e cadastrar consultas sobre requisições feitas a Prefeitura da Cidade do Recife.

## Requisitos
* Python 3.9
* PostgreSQL

## Executando o projeto 

1. Para testar o projeto é necessario estar utilizando o app do [front-end da aplicação](https://github.com/JampaUchoa/cityhelper-front)
2. Instalar o [poetry](https://python-poetry.org/) e o Python 3.9.0 (da maneira que preferir)
3. Instalar as dependecias com `poetry install`
4. Instalar o PostgreSQL e criar um banco chamado `cityhelper` para o usuário `postgres`
5. Rodar as migrações na base dados `poetry run python manage.py migrate`
6. Acessar o pagina para carregar os documentos em [csv](http://localhost:8000/api/upload/) (Pode demorar um pouco)
7. Rodar o serviço com `poetry run python manage.py runserver`
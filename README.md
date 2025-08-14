# Aplicação Backend Python com FastAPI - Frontend Vue JS - Base de dados Postgresql

## Como subir o banco de dados localmente:
1. Na pasta 'data-base' execute:
   ```bash
   docker-compose -f docker-compose-postgresql.yml up
   ```

## Como subir o backend localmente:

1. Na pasta 'back-end', instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure o .env da aplicação para apontar para o banco em localhost:
    O arquivo .env do backend deve conter: POSTGRES_HOST=localhost

3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Acesse o Swagger em [http://localhost:8000/docs](http://localhost:8000/docs)   

## Como subir o frontend localmente:

1. Tenha o Node.js versão 20 ou superior.

2. Na pasta 'front-end', instale as dependências:
   ```bash
	npm install
	```
3. Inicie o servidor de desenvolvimento:
   ```bash
	npm run dev
	```
4. Acesse o projeto em [http://localhost:5173](http://localhost:5173) (ou porta exibida no terminal).


## Como subir a aplicação no docker:

1. Configure o .env da aplicação para apontar para o banco dentro da stack:
    O arquivo .env do backend deve conter: POSTGRES_HOST=database

2. Publique a aplicação no Docker
   ```bash
	docker-compose -f docker-compose.yml up --build
	```


### Informações adicionais:
1. Para recriar todas as migrations da aplicação, basta apagá-las e executar o comando no backend:
   ```bash
	alembic revision --autogenerate -m "cria estrutura inicial"
	```
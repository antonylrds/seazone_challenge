# Khanto Project (Seaszone Challenge)

Khanto Project é uma api para gerenciamento de reservas de imóveis.

## Installation

Após clonar o projeto, é possível preciso instalar as dependencias 
```bash
$ pip install -r requirements.txt
```

É recomendado que a instalação de dependencias sejam feitas em um ambiente virtual python

```bash
$ py -m venv .venv
```

Após a criação do ambiente, é necessário ativa-lo
```bash
$ &.\.venv\Scripts\activate
```

## Database

O projeto foi desenvolvido utilizando o banco de dados padrão do Django (SQLite)

Para criação do banco e das tabelas necessárias, basta acessar a pasta principal do projeto
```bash
$ cd ./khanto_project
```

E roda o comando para criação das tabelas
```bash
$ py manage.py migrate
```

(Obs: Não é necessário rodar o comando `makemigrations` caso não ajam alterações na estrutura do banco)


## Iniciando a aplicação
Para iniciar a aplicação basta rodar o comando

```bash
$ py manage.py runserver
```

Por padrão, aplicação irá rodar em `127.0.0.1:8000`


## Documentação

Você pode checar a documentação gerada pelo postman [AQUI](https://documenter.getpostman.com/view/3466774/2s9YJW55kT)


## Autor

[Antony Luan](https://github.com/antonylrds)


## Licença
[MIT](https://choosealicense.com/licenses/mit/)
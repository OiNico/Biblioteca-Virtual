# 📚 Biblioteca Virtual

Uma aplicação web desenvolvida em **Python** para gerenciar uma biblioteca pessoal de livros. O projeto permite cadastrar, consultar, editar e remover livros por meio de uma API construída com **FastAPI**, utilizando **SQLite** como banco de dados.

## 🚀 Objetivo

O principal objetivo deste projeto é colocar em prática conceitos de desenvolvimento backend, como:

* Desenvolvimento de APIs REST com FastAPI;
* Manipulação de banco de dados SQLite;
* Organização de projetos em Python;
* Integração entre backend e frontend;
* Boas práticas de versionamento com Git e GitHub.

Além disso, o projeto servirá como base para futuras implementações, como autenticação de usuários, estatísticas de leitura e uma interface web responsiva.

---

## 🛠️ Tecnologias utilizadas

* Python 3.12+
* FastAPI
* SQLite3
* Uvicorn
* Pydantic

---

## 📂 Estrutura do projeto

```text
biblioteca_virtual/
│
├── main.py
├── database.py
├── crud.py
├── models.py
│
├── database.db
├── .gitignore
└── README.md
```

> A estrutura pode sofrer alterações conforme o projeto evoluir.

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Acesse a pasta do projeto

```bash
cd SEU-REPOSITORIO
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
uvicorn main:app --reload
```

---

## 📖 Documentação da API

Após iniciar a aplicação, a documentação interativa estará disponível em:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## ✨ Funcionalidades

### Implementadas

* Cadastro de livros
* Listagem de livros
* Banco de dados SQLite
* API REST com FastAPI

### Em desenvolvimento

* Buscar livro por ID
* Atualizar informações de um livro -> FAZENDO
* Excluir livros
* Pesquisa por título e autor
* Filtros por status de leitura
* Upload da capa do livro
* Sistema de notas
* Dashboard com estatísticas
* Interface web responsiva
* Autenticação de usuários

---

## 📌 Estrutura dos dados

Cada livro possui informações como:

* Título
* Autor
* Gênero
* Número de páginas
* Status da leitura

Novos campos poderão ser adicionados futuramente, como notas, resenha e foto da capa do livro.

---

## 🎯 Objetivos futuros

* Desenvolver um frontend responsivo.
* Implementar autenticação de usuários.
* Criar estatísticas de leitura.
* Adicionar gráficos de desempenho.
* Permitir upload de capas dos livros.
* Implementar busca avançada e filtros.

---

## 📚 Aprendizados

Este projeto está sendo desenvolvido com foco em aprendizado, explorando conceitos como:

* APIs REST
* CRUD
* Banco de dados relacionais
* Organização de código
* Versionamento com Git
* Desenvolvimento web com Python

---

## 👨‍💻 Autor

Desenvolvido por **Nicolas Gomes** como projeto de estudos e portfólio.

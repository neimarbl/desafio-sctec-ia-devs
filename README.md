# Desafio SCTEC - Gestão de Empreendimentos de Santa Catarina 

Este projeto é um protótipo de sistema CRUD (Create, Read, Update, Delete) desenvolvido como parte do processo de seleção para o curso **IA para DEVs** da SCTEC/SENAI. A aplicação foca na organização de informações sobre o ecossistema empreendedor catarinense, permitindo o gerenciamento de empresas nos setores de Tecnologia, Comércio, Indústria, Serviços e Agronegócio.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI (escolhido pela alta performance e documentação automática).
- **Banco de Dados:** SQLite (persistência local leve e eficiente).
- **ORM:** SQLAlchemy (mapeamento objeto-relacional para qualidade de código).
- **Validação:** Pydantic (garantia da integridade dos dados de entrada).
- **Servidor:** Uvicorn.

## Estrutura do Projeto
A arquitetura segue boas práticas de separação de responsabilidades (Design Patterns):
- `main.py`: Ponto de entrada da API e definição das rotas (endpoints).
- `models.py`: Definição das tabelas do banco de dados utilizando SQLAlchemy.
- `schemas.py`: Contratos de dados e regras de validação utilizando Pydantic.
- `database.py`: Configuração da conexão com o banco de dados SQLite.
- `.gitignore`: Arquivo para evitar o versionamento de arquivos desnecessários (como `.venv` e `.db`).

## Funcionalidades
O sistema permite o gerenciamento completo dos empreendimentos com os seguintes campos obrigatórios: Nome, Responsável, Município de SC, Segmento, Contato e Status.
1. **Cadastrar:** Registro de novos empreendimentos com validação de campos.
2. **Listar:** Visualização de todos os empreendimentos cadastrados.
3. **Atualizar:** Edição de informações existentes por ID.
4. **Remover:** Exclusão de registros do banco de dados.
5. **Integridade de Dados:** Implementação de Enums para seleção padronizada de Municípios e Segmentos, além de validação sintática de e-mails via Pydantic."

## Como Executar o Projeto
1. Clone o repositório: `git clone <link-do-seu-repositorio>`
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente: 
   - Windows: `.\.venv\Scripts\activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Inicie o servidor: `uvicorn main:app --reload`
6. Acesse a documentação interativa (Swagger) em: `http://localhost:8000/docs`

## Vídeo Pitch
Clique na imagem abaixo para assistir à demonstração técnica da solução (máximo 3 minutos):

[![Assista ao Vídeo Pitch](https://img.youtube.com)](https://youtu.be/aOjNS7UMO28)

> *Caso a imagem não carregue, utilize o link direto:* [Assista aqui no YouTube](https://youtu.be/aOjNS7UMO28)




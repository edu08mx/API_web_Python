# API de Gerenciamento de Usuários com Flask

Este é um projeto simples em Flask para criar uma API web que permite o cadastro, atualização, exclusão e consulta de usuários. A aplicação utiliza métodos HTTP (POST, PUT, DELETE, GET) para manipular uma lista fictícia de usuários. Ótimo para iniciantes em Flask!

## Funcionalidades

- Cadastro de novos usuários
- Atualização de dados de usuário
- Exclusão de usuários
- Consulta de usuários por ID
- Listagem de todos os usuários

## Exemplo de Uso

### Cadastrar Usuário (POST)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 7, "nome": "NovoUsuario"}' http://localhost:5000/cadastrarusuarios

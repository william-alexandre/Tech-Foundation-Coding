🚀 API RESTful com Flask

Projeto desenvolvido durante a aula de Tech Foundation & Coding da pós-graduação, com o objetivo de praticar os conceitos fundamentais de construção de APIs RESTful utilizando Python e Flask.

📚 Objetivo do Projeto

Este projeto tem como finalidade:

Compreender os conceitos básicos de APIs REST

Criar rotas utilizando o Flask

Trabalhar com métodos HTTP (GET)

Retornar dados no formato JSON

Simular endpoints para produtos e usuários

🛠️ Tecnologias Utilizadas

Python 3.x

Flask

JSON

📂 Estrutura do Projeto
APIs RESTful.py

Arquivo principal contendo:

Configuração da aplicação Flask

Definição das rotas

Simulação de base de dados com listas em memória

Inicialização do servidor local

🔗 Endpoints Disponíveis
🔹 GET /

Retorna mensagem confirmando que a API está funcionando.

Resposta:

<h1>API Funcionando!</h1>
🔹 GET /usuario

Retorna informações de um usuário fixo.

Exemplo de resposta:

{
  "Nome": "Anna",
  "Idade": 30,
  "E-mail": "Ana@teste.com"
}
🔹 GET /produtos

Retorna a lista completa de produtos.

🔹 GET /produtos/<id>

Retorna um produto específico com base no ID informado.

Caso o produto não seja encontrado, retorna erro 404.

🔹 GET /desconto

Calcula e retorna um valor com desconto aplicado.

Exemplo de resposta:

{
  "Preco_original": 100,
  "Valor com desconto": 90.0,
  "percentual": 10
}
🔹 GET /usuarios

Retorna a lista completa de usuários.

▶️ Como Executar o Projeto

Instale o Flask:

pip install flask

Execute o arquivo:

python "APIs RESTful.py"

Acesse no navegador:

http://127.0.0.1:5000/
🎯 Conceitos Praticados

Estrutura básica de uma API REST

Rotas e parâmetros dinâmicos

Serialização com jsonify

Códigos de status HTTP

Simulação de dados em memória

📌 Observações

Os dados estão armazenados em listas locais (não há banco de dados).

O projeto tem fins educacionais.

Pode ser expandido futuramente com:

Métodos POST, PUT e DELETE

Integração com banco de dados

Validações

Autenticação

👨‍💻 Autor

Projeto desenvolvido como prática acadêmica na pós-graduação 

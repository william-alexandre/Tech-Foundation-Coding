from flask import Flask, jsonify

app = Flask(__name__)

#Lista de produtos
produtos = [
    {'id':1, "nome": "Notebook", "preco": 2500.00},
    {'id':1, "nome": "Mouse", "preco": 120.00},
    {'id':1, "nome": "Teclado", "preco": 100.00}
]

#Lista de Usuarios
usuarios = [
    {'id':1, "nome": "João", "preco": 8.5},
    {'id':1, "nome": "Maria", "preco": 9.0},
    {'id':1, "nome": "Pedro", "preco": 7.5}
]

#Rota raiz
@app.route('/', methods=['GET'])
def home():
  return "<h1>API Funcionando!</h1>"

#Retorna informações de um user fixo
@app.route('/usuario')
def usuario():
  return jsonify ({
    "Nome":"Anna",
    "Idade": 30, 
    "E-mail":"Ana@teste.com"
    })

#Retorna todos os produtos
@app.route('/produtos')
def get_produtos():
  return jsonify(produtos)

#Retorna um produto específico por ID
@app.route('/produtos/<int:id>')
def get_produto(id):
  for produto in produtos:
    if produto['id'] == id:
      return jsonify(produto)
  return jsonify({'Erro':'Produto não encontrado'}), 404

#Retorna o preço com desconto
@app.route('/desconto')
def desconto():
  preco = 100
  percentual = 10
  valor_com_desconto = preco * (1 - percentual/100)
  return jsonify({
    "Preco_original":preco,
    "Valor com desconto":valor_com_desconto, 
    "percentual":percentual
    })

#Retorna todos os usuarios
@app.route('/usuarios')
def listar_usuarios():
  return jsonify(usuarios)

# Inicializa a aplicação local
if __name__ == '__main__':
  app.run(debug=True)

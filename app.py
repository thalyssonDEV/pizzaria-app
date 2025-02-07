from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from conn import connect_to_db
import auth
import pdfkit

app = Flask(__name__)

# Dicionário para armazenar temporariamente os dados do usuário e os pedidos.
dados_temporarios = {}


@app.route('/')
def home():
    # Exemplo: redireciona para a página de cadastro de funcionários (ou outro)
    return render_template('register_funcionarios.html')


@app.route("/register_usuarios", methods=["GET", "POST"])
def cadastrar():
    global dados_temporarios
    if request.method == "POST":
        nome = request.form.get("nome")
        endereco = request.form.get("endereco")
        telefone = request.form.get("telefone")
        
        # Armazena os dados do usuário
        dados_temporarios['usuario'] = {
            "nome": nome,
            "endereco": endereco,
            "telefone": telefone
        }
        # Inicializa a lista de pedidos vazia
        dados_temporarios['pedidos'] = []
        return render_template("select_pizzas.html")
    
    return render_template("register_usuarios.html")


@app.route("/register_funcionarios", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        authentication = auth.registrar_funcionario(nome, senha)
        if authentication:
            return render_template("login_funcionarios.html")
        else:
            return render_template("register_funcionarios.html")
    return render_template("register_funcionarios.html")


@app.route("/login_funcionarios", methods=["GET", "POST"])
def logar():
    if request.method == "POST":
        nome = request.form.get("nome")
        tentativa_senha = request.form.get("senha")
        authentication = auth.verificar_login(nome, tentativa_senha)
        if authentication:
            return render_template("register_usuarios.html")
        else:
            return render_template("login_funcionarios.html")
    return render_template("login_funcionarios.html")


@app.route('/get_sabores', methods=['GET'])
def get_sabores():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT tipo FROM pizza")
    sabores = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(sabores)


@app.route("/add_pizza", methods=["POST"])
def add_pizza():
    global dados_temporarios
    action = request.form.get("action")
    
    # Se o usuário clicou em "recibo", ignore os campos de sabor e tamanho
    if action == "recibo":
        return render_template(
            "recibo.html",
            usuario=dados_temporarios.get("usuario", {}),
            pedidos=dados_temporarios.get("pedidos", [])
        )
    
    # Se a ação for "adicionar", então verifica se os campos foram preenchidos
    sabor = request.form.get("sabor")
    tamanho = request.form.get("tamanho")
    
    if not sabor or not tamanho:
        # Opcional: pode enviar uma mensagem informando que é necessário selecionar
        return render_template("select_pizzas.html", message="Selecione um sabor e um tamanho para adicionar a pizza!")
    
    # Mapeamento de preços para cada tamanho
    price_mapping = {"P": 35, "M": 45, "G": 50, "GG": 70}
    preco = price_mapping.get(tamanho, 0)
    
    # Garante que a lista de pedidos exista
    if "pedidos" not in dados_temporarios:
        dados_temporarios["pedidos"] = []
    
    # Adiciona a pizza selecionada à lista de pedidos
    dados_temporarios["pedidos"].append({
        "sabor": sabor,
        "tamanho": tamanho,
        "preco": preco
    })
    
    # Após adicionar, recarrega a página de seleção com uma mensagem (opcional)
    return render_template("select_pizzas.html", message="Pizza adicionada!")


if __name__ == '__main__':
    app.run(debug=True)
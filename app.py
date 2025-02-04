from flask import Flask, render_template, request, redirect, url_for, session
from conn import connect_to_db
import auth


# Inicializa o servidor Flask
app = Flask(__name__)


@app.route('/')
def home() -> None:
    # Renderiza a página principal localmente no Flask
    return render_template('register_funcionarios.html')


@app.route("/register_usuarios", methods=["GET", "POST"])
def cadastrar() -> None:
    if request.method == "POST":
        nome = request.form.get("nome")
        bairro = request.form.get("bairro")
        rua = request.form.get("rua")
        numero_casa = request.form.get("numero_casa")
        telefone = request.form.get("telefone")
    
    return render_template("register_usuarios.html")


@app.route("/register_funcionarios", methods=["GET", "POST"])
def registrar() -> None:
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
def logar() -> None:
    if request.method == "POST":
        nome = request.form.get("nome")
        tentativa_senha = request.form.get("senha")      

        authentication = auth.verificar_login(nome, tentativa_senha)  

        if authentication:
            return render_template("register_usuarios.html")
        else:
            return render_template("login_funcionarios.html")
    
    return render_template("login_funcionarios.html")


if __name__ == '__main__':
    app.run(debug=True)
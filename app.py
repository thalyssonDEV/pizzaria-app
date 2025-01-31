from flask import Flask, render_template, request, redirect, url_for, session
from conn import connect_to_db

# Inicializa o servidor Flask
app = Flask(__name__)

@app.route('/')
def home() -> None:
    # Renderiza a página principal localmente no Flask
    return render_template('main_page.html')

@app.route("/register", methods=["GET", "POST"])
def register() -> None:
    # Rota para registro de usuários (ainda não implementada)
    pass

if __name__ == '__main__':
    # Executa o servidor Flask em modo de depuração
    app.run(debug=True)
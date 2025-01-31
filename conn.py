import psycopg2
import json
import os, sys

def load_db_config():
    # Define o caminho do arquivo de configuração JSON do banco de dados
    config_path = os.path.join(os.path.dirname(__file__), "json/db_config.json")

    try:
        # Abre e carrega as configurações do banco de dados a partir do arquivo JSON
        with open(config_path, "r") as config_file:
            return json.load(config_file)
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Exibe erro caso o arquivo não seja encontrado ou contenha erro de formatação
        print(f"Erro ao Carregar o Arquivo de Configuração: {e}")
        sys.exit(1)  # Encerra a execução do programa

def connect_to_db():
    # Carrega as configurações do banco de dados
    db_config = load_db_config()

    try:
        # Estabelece a conexão com o banco de dados utilizando os parâmetros carregados
        conn = psycopg2.connect(
            host = db_config["host"],
            database = db_config["database"],
            user = db_config["user"],
            password = db_config["password"],
            port = db_config["port"]
        )
        print("Conexão Bem-Sucedida ao Banco de Dados")

        return conn  # Retorna o objeto de conexão
    
    except Exception as e:
        # Exibe erro caso a conexão falhe
        print(f"Conexão Mal-Sucedida ao Banco de Dados: {e}")
        return None  # Retorna None em caso de falha na conexão
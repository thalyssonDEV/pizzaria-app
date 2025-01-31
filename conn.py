import psycopg2
import json
import os, sys

def load_db_config():
    config_path = os.path.join(os.path.dirname(__file__), "db_config.json")

    try:
        with open(config_path, "r") as config_file:
            return json.load(config_file)
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao Carregar o Arquivo de Configuração: {e}")
        sys.exit(1)
    
def connect_to_db():
    db_config = load_db_config()

    try:
        conn = psycopg2.connect(
            host = db_config["host"],
            database = db_config["database"],
            user = db_config["user"],
            password = db_config["password"],
            port = db_config["port"]
        )
        print("Conexão Bem-Sucedida ao Banco de Dados")

        return conn
    
    except Exception as e:
        print(f"Conexão Mal-Sucedida ao Banco de Dados: {e}")
        return None
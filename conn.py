import psycopg2
import os, sys

def check_env_vars():
    # Verifica se todas as variáveis de ambiente necessárias estão definidas
    required_vars = ["host", "database", "user", "password", "port"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Erro: Variáveis de ambiente ausentes: {', '.join(missing_vars)}")
        sys.exit(1)


def connect_to_db():
    # Conecta ao banco de dados usando variáveis de ambiente
    check_env_vars()
    
    # Carrega as configurações do banco de dados
    # db_config = load_db_config()

    try:
        # Estabelece a conexão com o banco de dados utilizando os parâmetros carregados
        conn = psycopg2.connect(
            host = os.getenv("host", "your_localhost"),              # Endereço do banco de dados
            database = os.getenv("database", "your_database"),     # Nome do banco de dados
            user = os.getenv("user", "your_user"),                # Usuário do banco de dados
            password = os.getenv("password", "your_password"),     # Senha do banco de dados
            port = os.getenv("port", "your_port")                   # Porta do banco de dados
        )
        print("Conexão Bem-Sucedida ao Banco de Dados")

        return conn  # Retorna o objeto de conexão
    
    except Exception as e:
        # Exibe erro caso a conexão falhe
        print(f"Conexão Mal-Sucedida ao Banco de Dados: {e}")
        return None  # Retorna None em caso de falha na conexão
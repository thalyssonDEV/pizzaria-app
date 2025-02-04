from conn import connect_to_db

def registrar_funcionario(nome, senha):
    conn = connect_to_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO funcionario (nome, senha)
            VALUES (%s, %s);
            """

            cursor.execute(query, (nome, senha))
            conn.commit()
            print('Usuário Registrado')

        except Exception as e:
            print(f"Erro ao Registrar o Usuário: {e}")
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    else:
        print("Falha na Conexão com o Banco de Dados")
        return None


def verificar_login(nome, tentativa_senha):
    conn = connect_to_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = """
            SELECT id, senha FROM funcionario WHERE nome = %s;
            """

            cursor.execute(query, (nome,))
            result = cursor.fetchone()

            if result:
                id, access = result
                print("Usuário Encontrado")
            
                if str(tentativa_senha).strip() == str(access).strip():
                        print("Login Bem-Sucedido!")
                        return id
                else:
                    print("Login Mal-Sucedido: Senha Incorreta")
                    return None
    
            else:
                print("Usuário Não Encontrado")
                return None

        except Exception as e:
            print(f"Erro ao Tentar Fazer Login: {e}")
            return None
        
        finally:
            cursor.close()
            conn.close()
            
    else:
        print("Falha na Conexão com o Banco de Dados")
        return None
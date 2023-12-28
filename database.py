#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import sqlite3 # importa a biblioteca de banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Database(): # classe para o banco de dados
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):

        pass

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def open_conn(self): # método para conectar ao banco de dados

        self.conn = sqlite3.connect('DB000') # objeto de conexao com o banco de dados de nome clientes
        self.cursor = self.conn.cursor()     # objeto de cursor para executar comando SQL

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def close_conn(self): # método para desconectar o banco de dados

        self.conn.close() # objeto de encerramento de conexao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def create_table(self): # método de manipulacao e criacao de tabelas

        self.open_conn() # chama o método de conexao com o banco de dados

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tab_admins (
                            username CHAR(40) PRIMARY KEY,
                            password TEXT
                            );
                            """)
        
        self.conn.commit() # insere o comando SQL

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tab_employees (
                            ID INTEGER PRIMARY KEY,
                            IDC TEXT,
                            name TEXT, 
                            age INTEGER,
                            sex TEXT,
                            address TEXT,
                            phone INTEGER,
                            marital_status TEXT,
                            dependents INTEGER,
                            city TEXT,
                            job_position TEXT,
                            salary DECIMAL (5,2),
                            work_shift TEXT
                            );
                            """)
        
        self.conn.commit() # insere o comando SQL

        self.close_conn()  # chama o método para encerrar a conexao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def insert_into(self): # método para inserir dados nas tabelas

        self.open_conn() # chama o método de conexao com o banco de dados

        admin_list = [        # lista de admins
            ('user1', '123'),
            ('user2', '132'),
            ('user3', '321')
        ]

        insert_query = "INSERT INTO tab_admins (username, password) VALUES (?, ?)" # string de query

        for user_data in admin_list:                     # ciclo para iterar sobre os elementos da lista
            self.cursor.execute(insert_query, user_data) # executa a query na tupla

        self.conn.commit() # insere o comando SQL
        self.close_conn()   

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def verify_user_credentials(self, username, password): # método para verificar usuário e senha

        self.open_conn() # chama o método de conexao com o banco de dados

        query = "SELECT username, password FROM tab_admins WHERE username = ? AND password = ?" # string de query

        self.cursor.execute(query, (username, password)) # executa a query na tupla

        result = self.cursor.fetchone() # obtém resultado da próxima linha do comando SQL

        self.close_conn() # chama o método para encerrar a conexao

        # Retorna True se o resultado não for None (ou seja, se um usuário foi encontrado),
        # e False caso contrário (nenhum usuário correspondente)
        return result is not None

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def view_rows(table_name): # método para verificar o conteudo das tabelas

        conn = sqlite3.connect('DB000') # cria um conexao com o sqlite3
        cursor = conn.cursor()          
        
        query = f"SELECT * FROM {table_name};" # string de conexao que recebe um argumento
        
        cursor.execute(query) # executa a query 
        
        rows = cursor.fetchall() # recupera todas as linhas
        
        conn.close() # chama o método para encerrar a conexao
        
        return rows # retorna as linhas da tabela

    # Substitua 'tab_admins' pelo nome da tabela que deseja consultar
        table_name = 'tab_admins'
        result = view_rows(table_name)

        # Exibe o resultado
        print(f"Conteúdo da tabela {table_name}:")
        for row in result:
            print(row)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def fetch_column_names(table_name):
        conn = sqlite3.connect('DB000')
        cursor = conn.cursor()
        
        # Consulta para obter os nomes das colunas da tabela
        query = f"PRAGMA table_info({table_name});"
        
        # Executa a consulta
        cursor.execute(query)
        
        # Recupera todas as linhas (cada linha contém informações sobre uma coluna)
        rows = cursor.fetchall()
        
        # Fecha a conexão com o banco de dados
        conn.close()
        
        # Extrai os nomes das colunas da primeira posição de cada tupla
        column_names = [row[1] for row in rows]
        
        return column_names

        # Substitua 'tab_admins' pelo nome da tabela que deseja consultar
        table_name = 'tab_employees'
        columns = fetch_column_names(table_name)

        # Exibe o resultado
        print(f"Colunas da tabela {table_name}: {columns}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

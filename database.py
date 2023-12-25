#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import sqlite3 # importa a biblioteca de banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Database(): # classe para o banco de dados
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

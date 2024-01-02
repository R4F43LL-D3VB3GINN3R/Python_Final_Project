#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from tkinter import *         # importa a biblioteca tkinter
from tkinter import ttk       # importa mais funcionalidades do tkinter
from database import Database # importa a biblioteca de base de dados
from tkinter import messagebox # importa a caixa de mensagens do tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class RHScreen(): # inicializa a classe RH
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):
  
        self.rhroot = Tk()      # o objeto recebe a raiz da aplicacao 
        self.database = Database() # instancia do banco de dados
        self.rh_mainscreen()    # invoca o metodo de criacao e configuracao da tela de login
        self.rh_frame()         # invoca o metodo de criacao e configuracao do frame de tela
        self.rh_widgets()       # invoca o metodo de criacao e configuracao de widgets
        self.rhroot.mainloop()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def rh_mainscreen(self): # método de configuracao de tela principal

        self.rhroot.title("Human Resources")                                            # título 
        screen_width = self.rhroot.winfo_screenwidth()                                  # coordenada da largura    
        screen_height = self.rhroot.winfo_screenheight()                                # coordenada da altura
        form_width = 800                                                                # largura
        form_height = 600                                                               # altura     
        x_cordinate = int((screen_width/2) - (form_width/2))                            # setup de posição horizontal
        y_cordinate = int((screen_height/2) - (form_height/2))                          # setup de posição vertical    
        self.rhroot.geometry(f'{form_width}x{form_height}+{x_cordinate}+{y_cordinate}') # resolução da tela e posicionamento dos setups
        self.rhroot.configure(bg='white')                                               # configuração 
        self.rhroot.configure(cursor='hand2')                                           # cursor
        self.rhroot.configure(takefocus=True)                                           # foco
        self.rhroot.configure(borderwidth=50, relief="groove")                          # borda
        self.rhroot.iconbitmap('icons/001 - login.ico')                                 # ícone 
        self.rhroot.resizable(True, True)                                               # responsividade 
        self.rhroot.maxsize(width=1200, height=800)                                     # tamanho máximo
        self.rhroot.minsize(width=600, height=400)                                      # tamanho mínimo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def rh_frame(self): # configuracao do frame de tela

        self.frame1 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame1.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=1)                                    # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def rh_widgets(self): # insercao de widgets

        # Botões do Frame1
        self.bt_insert = Button(self.frame1, text='Insert', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_insert) # setup 
        self.bt_insert.place(relx=0.01, rely=0.01, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_remove = Button(self.frame1, text='Search', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_search) # setup 
        self.bt_remove.place(relx=0.01, rely=0.09, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_exitmenu = Button(self.frame1, text='Exit', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.rhroot.destroy) # setup 
        self.bt_exitmenu.place(relx=0.01, rely=0.17, relwidth=1, relheight=0.07)                                                                                                                        # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def frame_insert(self): # método de criacao de frame

        self.frame2 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame2.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                      # posicao

        #--------------------------------------

        # Widgets - [Molduras] 

        self.canvas_bt = Canvas(self.frame2, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas_bt.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.65)                                                # posiciona a moldura

        self.canvas_bt = Canvas(self.frame2, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas_bt.place(relx=0.01, rely=0.67, relwidth=0.98, relheight=0.32)                                                # posiciona a moldura        

        #--------------------------------------

        # Widgets - [Labels] 

        self.lb_title1 = Label(self.frame2, text = 'Personal Info', bg='grey', font=('comic-sans', 15, 'bold', 'italic')) # setup
        self.lb_title1.place(relx=0.33, rely=0.03, relwidth=0.3, relheight=0.05)                                          # posicao

        self.lb_name = Label(self.frame2, text = 'Name:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_name.place(relx=0.14, rely=0.1, relwidth=0.09, relheight=0.05)                                  # posicao

        self.lb_id = Label(self.frame2, text = 'ID:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_id.place(relx=0.16, rely=0.16, relwidth=0.07, relheight=0.05)                               # posicao

        self.lb_idc = Label(self.frame2, text = 'IDC:', bg='grey', font=('comic-sans', 10, 'bold', 'italic'))  # setup
        self.lb_idc.place(relx=0.3, rely=0.16, relwidth=0.07, relheight=0.05)                                  # posicao

        self.lb_age = Label(self.frame2, text = 'Age:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_age.place(relx=0.3, rely=0.22, relwidth=0.07, relheight=0.05)                                # posicao

        self.lb_sex = Label(self.frame2, text = 'Sex:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_sex.place(relx=0.16, rely=0.22, relwidth=0.06, relheight=0.05)                                # posicao

        self.lb_address = Label(self.frame2, text = 'Address:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_address.place(relx=0.11, rely=0.28, relwidth=0.11, relheight=0.05)                                    # posicao

        self.lb_phone = Label(self.frame2, text = 'Phone:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_phone.place(relx=0.13, rely=0.34, relwidth=0.09, relheight=0.05)                                  # posicao

        self.lb_marital = Label(self.frame2, text = 'Marital Status:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_marital.place(relx=0.05, rely=0.4, relwidth=0.17, relheight=0.05)                                            # posicao

        self.lb_sons = Label(self.frame2, text = 'Dependents:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_sons.place(relx=0.07, rely=0.46, relwidth=0.15, relheight=0.05)                                       # posicao    

        self.lb_nationality = Label(self.frame2, text = 'Nationality:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_nationality.place(relx=0.08, rely=0.52, relwidth=0.14, relheight=0.05)                                        # posicao 

        self.lb_city = Label(self.frame2, text = 'City:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_city.place(relx=0.16, rely=0.58, relwidth=0.065, relheight=0.05)                                # posicao    

        self.lb_title2 = Label(self.frame2, text = 'Job Info', bg='grey', font=('comic-sans', 15, 'bold', 'italic')) # setup
        self.lb_title2.place(relx=0.33, rely=0.69, relwidth=0.3, relheight=0.05)                                     # posicao 

        self.lb_pos = Label(self.frame2, text = 'Job Position:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_pos.place(relx=0.065, rely=0.77, relwidth=0.16, relheight=0.05)                                        # posicao 

        self.lb_salary = Label(self.frame2, text = 'Salary:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_salary.place(relx=0.13, rely=0.83, relwidth=0.1, relheight=0.05)                                    # posicao    

        self.lb_turn = Label(self.frame2, text = 'Work Shift:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_turn.place(relx=0.081, rely=0.89, relwidth=0.14, relheight=0.05)                                      # posicao 

        #--------------------------------------

        # Widgets - [Entradas]

        self.in_name = Entry(self.frame2, bd=4)                               # setup
        self.in_name.place(relx=0.23, rely=0.1, relwidth=0.7, relheight=0.05) # posicao

        self.in_id = Entry(self.frame2, bd=4)                                 # setup
        self.in_id.place(relx=0.23, rely=0.16, relwidth=0.05, relheight=0.05) # posicao

        self.in_idc = Entry(self.frame2, bd=4)                                 # setup
        self.in_idc.place(relx=0.37, rely=0.16, relwidth=0.11, relheight=0.05) # posicao

        self.in_age = Entry(self.frame2, bd=4)                                 # setup
        self.in_age.place(relx=0.37, rely=0.22, relwidth=0.05, relheight=0.05) # posicao

        self.in_sex = Entry(self.frame2, bd=4)                                 # setup
        self.in_sex.place(relx=0.23, rely=0.22, relwidth=0.05, relheight=0.05) # posicao

        self.in_address = Entry(self.frame2, bd=4)                                # setup
        self.in_address.place(relx=0.23, rely=0.28, relwidth=0.7, relheight=0.05) # posicao

        self.in_phone = Entry(self.frame2, bd=4)                                 # setup
        self.in_phone.place(relx=0.23, rely=0.34, relwidth=0.12, relheight=0.05) # posicao

        self.in_marital = Entry(self.frame2, bd=4)                               # setup
        self.in_marital.place(relx=0.23, rely=0.4, relwidth=0.2, relheight=0.05) # posicao

        self.in_sons = Entry(self.frame2, bd=4)                                 # setup
        self.in_sons.place(relx=0.23, rely=0.46, relwidth=0.04, relheight=0.05) # posicao    

        self.in_nationality = Entry(self.frame2, bd=4)                                # setup
        self.in_nationality.place(relx=0.23, rely=0.52, relwidth=0.2, relheight=0.05) # posicao 

        self.in_city = Entry(self.frame2, bd=4)                                # setup
        self.in_city.place(relx=0.23, rely=0.58, relwidth=0.2, relheight=0.05) # posicao    

        self.in_pos = Entry(self.frame2, bd=4)                                # setup
        self.in_pos.place(relx=0.23, rely=0.77, relwidth=0.2, relheight=0.05) # posicao 

        self.in_salary = Entry(self.frame2, bd=4)                                # setup
        self.in_salary.place(relx=0.23, rely=0.83, relwidth=0.1, relheight=0.05) # posicao    

        self.in_turn = Entry(self.frame2, bd=4)                                # setup
        self.in_turn.place(relx=0.23, rely=0.89, relwidth=0.1, relheight=0.05) # posicao 

        #--------------------------------------

        # Widgets - [Botões]
        self.bt_show_employee = Button(self.frame2, text='Show', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_employees) # setup 
        self.bt_show_employee.place(relx=0.77, rely=0.7, relwidth=0.2, relheight=0.07)                                                                                                                        # posicao

        self.bt_save_employee = Button(self.frame2, text='Save', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.insert_client) # setup 
        self.bt_save_employee.place(relx=0.77, rely=0.8, relwidth=0.2, relheight=0.07)                                                                                                                         # posicao

        self.bt_clear_employee = Button(self.frame2, text='Clear', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.clear_fields) # setup 
        self.bt_clear_employee.place(relx=0.77, rely=0.9, relwidth=0.2, relheight=0.07)                                                                                                                       # posicao
                                                                                                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def show_employees(self):
         
        # Widgets 
        self.subframe2 = Toplevel(self.rhroot)
        self.subframe2.title("Employee Details")
        self.subframe2.geometry("1500x500")

        #--------------------------------------

        # Treeview
        self.listEmpl = ttk.Treeview(self.subframe2, height = 3, column = ("col0","col1", "col2'", "col3", "col4", "col5", "col6'", "col7", "col8", "col9", "col10'", "col11", "col12", "col13")) # objeto treeview criado na tela2
        self.insert_treeview() # método para exibir os dados dentro da treeview
        #--------------------------------------

        # Cabecalhos
        self.listEmpl.heading("#0", text="")               # texto de cabecalho
        self.listEmpl.heading("#1", text="ID")             # texto de cabecalho
        self.listEmpl.heading("#2", text="IDC")            # texto de cabecalho
        self.listEmpl.heading("#3", text="Name")           # texto de cabecalho
        self.listEmpl.heading("#4", text="Age")            # texto de cabecalho
        self.listEmpl.heading("#5", text="Sex")            # texto de cabecalho
        self.listEmpl.heading("#6", text="Address")        # texto de cabecalho
        self.listEmpl.heading("#7", text="Phone")          # texto de cabecalho
        self.listEmpl.heading("#8", text="Marital Status") # texto de cabecalho
        self.listEmpl.heading("#9", text="Dependents")     # texto de cabecalho
        self.listEmpl.heading("#10", text="Nationality")   # texto de cabecalho
        self.listEmpl.heading("#11", text="City")          # texto de cabecalho
        self.listEmpl.heading("#12", text="Job Position")  # texto de cabecalho
        self.listEmpl.heading("#13", text="Salary")        # texto de cabecalho
        self.listEmpl.heading("#14", text="Work Shift")    # texto de cabecalho

        #--------------------------------------

        # Colunas
        self.listEmpl.column("#0", width=10)   # tamanho da coluna
        self.listEmpl.column("#1", width=50)   # tamanho da coluna
        self.listEmpl.column("#2", width=50)   # tamanho da coluna
        self.listEmpl.column("#3", width=150)  # tamanho da coluna
        self.listEmpl.column("#4", width=50)   # tamanho da coluna
        self.listEmpl.column("#5", width=50)   # tamanho da coluna
        self.listEmpl.column("#6", width=150)  # tamanho da coluna
        self.listEmpl.column("#7", width=50)   # tamanho da coluna
        self.listEmpl.column("#8", width=100)  # tamanho da coluna
        self.listEmpl.column("#9", width=50)   # tamanho da coluna
        self.listEmpl.column("#10", width=100) # tamanho da coluna
        self.listEmpl.column("#11", width=100) # tamanho da coluna
        self.listEmpl.column("#12", width=100) # tamanho da coluna
        self.listEmpl.column("#13", width=50)  # tamanho da coluna
        self.listEmpl.column("#14", width=50)  # tamanho da coluna

        #--------------------------------------

        # Treeview Configuracoes
        self.listEmpl.place(relx = 0.01, rely = 0.05, relwidth = 0.95, relheight = 0.85)    # insere a treeview com posicao e tamanho desejado

        vsb = ttk.Scrollbar(self.subframe2, orient="vertical", command=self.listEmpl.yview) # objeto barra de rolagem criado na tela2
        vsb.place(relx = 0.96, rely = 0.05, relheight = 0.85)                               # insere a barra de rolagem com posicao e tamanho desejado
        self.listEmpl.configure(yscrollcommand=vsb.set)                                     # configuracao da barra de rolagem

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def clear_fields(self):

        self.in_name.delete(0, END)        # limpa a entrada 
        self.in_id.delete(0, END)          # limpa a entrada
        self.in_idc.delete(0, END)         # limpa a entrada
        self.in_age.delete(0, END)         # limpa a entrada
        self.in_sex.delete(0, END)         # limpa a entrada
        self.in_address.delete(0, END)     # limpa a entrada   
        self.in_phone.delete(0, END)       # limpa a entrada
        self.in_marital.delete(0, END)     # limpa a entrada
        self.in_sons.delete(0, END)        # limpa a entrada
        self.in_nationality.delete(0, END) # limpa a entrada      
        self.in_city.delete(0, END)        # limpa a entrada
        self.in_pos.delete(0, END)         # limpa a entrada
        self.in_salary.delete(0, END)      # limpa a entrada
        self.in_turn.delete(0, END)        # limpa a entrada

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def get_client(self):
         
        self.id = self.in_id.get()                   # objeto criado recebe o que for digitado na entrada
        self.idc = self.in_idc.get()                 # objeto criado recebe o que for digitado na entrada
        self.name = self.in_name.get()               # objeto criado recebe o que for digitado na entrada
        self.age = self.in_age.get()                 # objeto criado recebe o que for digitado na entrada
        self.sex = self.in_sex.get()                 # objeto criado recebe o que for digitado na entrada
        self.address = self.in_address.get()         # objeto criado recebe o que for digitado na entrada
        self.phone = self.in_phone.get()             # objeto criado recebe o que for digitado na entrada
        self.marital = self.in_marital.get()         # objeto criado recebe o que for digitado na entrada
        self.sons = self.in_sons.get()               # objeto criado recebe o que for digitado na entrada
        self.nationality = self.in_nationality.get() # objeto criado recebe o que for digitado na entrada
        self.city = self.in_city.get()               # objeto criado recebe o que for digitado na entrada
        self.pos = self.in_pos.get()                 # objeto criado recebe o que for digitado na entrada
        self.salary = self.in_salary.get()           # objeto criado recebe o que for digitado na entrada
        self.turn = self.in_salary.get()             # objeto criado recebe o que for digitado na entrada

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def insert_client(self): # metodo para inserir o cliente na tabela.
         
        self.get_client()         # invoca o metodo para receber os dados inseridos na entrada
        self.database.open_conn() # abre a conexao com a base de dados

        # Verifica se o empregado já existe na tabela
        existing_employee = self.database.cursor.execute(
            """SELECT ID FROM tab_employees WHERE IDC = ?""",
            (self.idc,)
        ).fetchone()

        if existing_employee:
            # Empregado já existe, então execute uma operação de UPDATE
            self.database.cursor.execute(
                """UPDATE tab_employees
                SET name = ?, age = ?, sex = ?, address = ?, phone = ?, marital_status = ?, dependents = ?,
                    nationality = ?, city = ?, job_position = ?, salary = ?, work_shift = ?
                WHERE IDC = ?""",
                (self.name, self.age, self.sex, self.address, self.phone, self.marital, self.sons, self.nationality,
                self.city, self.pos, self.salary, self.turn, self.idc)
            )
            messagebox.showinfo("Info", "Employee with IDC {} updated.".format(self.idc))
        else:
            # Empregado não existe, proceda com a inserção
            self.database.cursor.execute(
                """INSERT INTO tab_employees (IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (self.idc, self.name, self.age, self.sex, self.address, self.phone, self.marital, self.sons, self.nationality,
                self.city, self.pos, self.salary, self.turn)
            )
            messagebox.showinfo("Info", "Employee with IDC {} added.".format(self.idc))

        self.database.conn.commit() # executa a query SQL
        self.database.close_conn()  # encerra a conexao
        self.insert_treeview()      # invoca o método para povoar a treeview
        self.clear_fields()         # invoca o metodo para limpar os campos

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
         
    def insert_treeview(self): # método para inserir os dados das entradas na treeview

         
        self.listEmpl.delete(*self.listEmpl.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren

        self.database.open_conn() # abre conexão com banco de dados

        lista = self.database.cursor.execute(""" SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift FROM tab_employees ORDER BY name ASC; """)
        # seleciona todos os campos da tabela na lista e os ordena pelos nomes dos empregados em ordem alfabetica

        for i in lista:                              # percorre todos os itens da lista que guarda os resultados da consulta ao banco de dados 
             self.listEmpl.insert("", END, values=i) # os itens serão inseridos a lista do topo ao final

        self.database.close_conn() # fecha conexão com o banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def frame_search(self): # método de criacao de frame
         
            self.frame3 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
            self.frame3.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                      # posicao

            #--------------------------------------

            # Widgets - [Molduras] 

            self.canvas_frame3 = Canvas(self.frame3, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
            self.canvas_frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)                                                 # posiciona a moldura 

            self.canvas2_frame3 = Canvas(self.frame3, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
            self.canvas2_frame3.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.66)                                                # posiciona a moldura      

            #--------------------------------------

            # Widgets - [Labels] 

            self.lb_title1 = Label(self.frame3, text = 'Search Employee', bg='grey', font=('comic-sans', 15, 'bold', 'italic')) # setup
            self.lb_title1.place(relx=0.33, rely=0.03, relwidth=0.3, relheight=0.05)                                            # posicao

            self.lb_idsearch = Label(self.frame3, text = 'ID:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_idsearch.place(relx=0.06, rely=0.1, relwidth=0.1, relheight=0.05)                                 # posicao

            self.lb_or = Label(self.frame3, text = 'Name:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_or.place(relx=0.24, rely=0.1, relwidth=0.1, relheight=0.05)                                   # posicao

            #--------------------------------------

            # Widgets - [Entradas]

            self.in_idsearch = Entry(self.frame3, bd=4)                               # setup
            self.in_idsearch.place(relx=0.14, rely=0.1, relwidth=0.1, relheight=0.05) # posicao

            self.in_namesearch = Entry(self.frame3, bd=4)                               # setup
            self.in_namesearch.place(relx=0.34, rely=0.1, relwidth=0.6, relheight=0.05) # posicao

            #--------------------------------------

            # Widgets - [Botões]
            self.bt_show_employee = Button(self.frame3, text='Start', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.insert_treeview_search) # setup 
            self.bt_show_employee.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.07)                                                                                                                          # posicao
            
            #--------------------------------------                                                                                                                       
            
            # Treeview
            self.listEmplSearch = ttk.Treeview(self.frame3, height = 3, column = ("col0","col1", "col2'", "col3", "col4", "col5", "col6'", "col7", "col8", "col9", "col10'", "col11", "col12", "col13")) # objeto treeview criado na tela
            #--------------------------------------

            # Cabecalhos
            self.listEmplSearch.heading("#0", text="")               # texto de cabecalho
            self.listEmplSearch.heading("#1", text="ID")             # texto de cabecalho
            self.listEmplSearch.heading("#2", text="IDC")            # texto de cabecalho
            self.listEmplSearch.heading("#3", text="Name")           # texto de cabecalho
            self.listEmplSearch.heading("#4", text="Age")            # texto de cabecalho
            self.listEmplSearch.heading("#5", text="Sex")            # texto de cabecalho
            self.listEmplSearch.heading("#6", text="Address")        # texto de cabecalho
            self.listEmplSearch.heading("#7", text="Phone")          # texto de cabecalho
            self.listEmplSearch.heading("#8", text="Marital Status") # texto de cabecalho
            self.listEmplSearch.heading("#9", text="Dependents")     # texto de cabecalho
            self.listEmplSearch.heading("#10", text="Nationality")   # texto de cabecalho
            self.listEmplSearch.heading("#11", text="City")          # texto de cabecalho
            self.listEmplSearch.heading("#12", text="Job Position")  # texto de cabecalho
            self.listEmplSearch.heading("#13", text="Salary")        # texto de cabecalho
            self.listEmplSearch.heading("#14", text="Work Shift")    # texto de cabecalho

            #--------------------------------------

            # Colunas
            self.listEmplSearch.column("#0", width=0)    # tamanho da coluna
            self.listEmplSearch.column("#1", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#2", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#3", width=150)  # tamanho da coluna
            self.listEmplSearch.column("#4", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#5", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#6", width=150)  # tamanho da coluna
            self.listEmplSearch.column("#7", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#8", width=100)  # tamanho da coluna
            self.listEmplSearch.column("#9", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#10", width=100) # tamanho da coluna
            self.listEmplSearch.column("#11", width=100) # tamanho da coluna
            self.listEmplSearch.column("#12", width=100) # tamanho da coluna
            self.listEmplSearch.column("#13", width=50)  # tamanho da coluna
            self.listEmplSearch.column("#14", width=50)  # tamanho da coluna

            #--------------------------------------

            # Treeview Configuracoes
            self.listEmplSearch.place(relx = 0.02, rely = 0.35, relwidth = 0.95, relheight = 0.4)    # insere a treeview com posicao e tamanho desejado

            hsb = ttk.Scrollbar(self.frame3, orient="horizontal", command=self.listEmplSearch.xview)
            hsb.place(relx=0.02, rely=0.7, relwidth=0.94)  # Posiciona a barra de rolagem horizontal

            self.listEmplSearch.configure(xscrollcommand=hsb.set)  # Configura o comando de rolagem horizontal
                                                                                                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            
    def insert_treeview_search(self):
        
        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # Limpa os itens existentes na Treeview
        
        self.in_namesearch.insert(END, '%') # Insere '%' na entrada de nome para procurar qualquer correspondência
        nome = self.in_namesearch.get()     # o nome recebe a entrada do nome

        self.database.open_conn() # Conecta ao banco de dados

        if self.in_idsearch.get(): # Executa a consulta com base no ID ou no nome
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift
                FROM tab_employees
                WHERE ID = ?""",
                (self.in_idsearch.get(),)
            ).fetchall() # Busca apenas pelo ID se fornecido
            if lista:
                self.bt_remove = Button(self.frame3, text='Remove', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'))
                self.bt_remove.place(relx=0.03, rely=0.9, relwidth=0.2, relheight=0.07)
                self.bt_change = Button(self.frame3, text='Change', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.changebutton)
                self.bt_change.place(relx=0.03, rely=0.82, relwidth=0.2, relheight=0.07)
        else: # Busca pelo ID ou pelo nome com correspondência parcial
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift
                FROM tab_employees
                WHERE ID = ? OR name LIKE ?""",
                (self.in_idsearch.get(), f'%{nome}%')
            ).fetchall()
            if lista:
                self.bt_remove = Button(self.frame3, text='Remove', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'))
                self.bt_remove.place(relx=0.03, rely=0.9, relwidth=0.2, relheight=0.07)
                self.bt_change = Button(self.frame3, text='Change', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.changebutton)
                self.bt_change.place(relx=0.03, rely=0.82, relwidth=0.2, relheight=0.07)

        for i in lista: # ciclo for para correr a pesquisa
            self.listEmplSearch.insert("", END, values=i) # insere cada item achado da pesquisa na lista

        if not lista: # Exibe uma mensagem se nenhum registro for encontrado
            messagebox.showinfo("Info", "No records found for the search criteria.")

        self.database.close_conn() # Fecha a conexão com o banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def changebutton(self): # método do botâo change guarda dois métodos

        self.frame_insert()   # método para chamar a tela de cadastro de funcionários
        self.insert_entries() # método para transportar os dados da Treeview para as entradas da tela de cadastro de funcionários

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
         
    def insert_entries(self): # método para inserir os dados das entradas na treeview

         
        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren

        nome = self.in_namesearch.get()     # o nome recebe a entrada do nome

        self.database.open_conn() # abre conexão com banco de dados

        lista = self.database.cursor.execute(""" SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift FROM tab_employees WHERE ID = ? or name LIKE ? ORDER BY name ASC; """, (self.in_idsearch.get(), f'%{nome}%')
            ).fetchall()
        # seleciona todos os campos da tabela na lista e os ordena pelos nomes dos empregados em ordem alfabetica

        for i in lista:                              # percorre todos os itens da lista que guarda os resultados da consulta ao banco de dados 
             self.listEmplSearch.insert("", END, values=i) # os itens serão inseridos a lista do topo ao final

        self.database.close_conn() # fecha conexão com o banco de dados

        # Preenche as entradas com os valores do primeiro item da Treeview
        first_item = self.listEmplSearch.item(self.listEmplSearch.get_children()[0], "values")

        self.in_id.delete(0, END)
        self.in_id.insert(0, first_item[0])  # ID
        self.in_idc.delete(0, END)
        self.in_idc.insert(0, first_item[1])  # IDC
        self.in_name.delete(0, END)
        self.in_name.insert(0, first_item[2])  # Name
        self.in_age.delete(0, END)
        self.in_age.insert(0, first_item[3])  # Age
        self.in_sex.delete(0, END)
        self.in_sex.insert(0, first_item[4])  # Sex
        self.in_address.delete(0, END)
        self.in_address.insert(0, first_item[5])  # Address
        self.in_phone.delete(0, END)
        self.in_phone.insert(0, first_item[6])  # Phone
        self.in_marital.delete(0, END)
        self.in_marital.insert(0, first_item[7])  # Marital Status
        self.in_sons.delete(0, END)
        self.in_sons.insert(0, first_item[8])  # Dependents
        self.in_nationality.delete(0, END)
        self.in_nationality.insert(0, first_item[9])  # Nationality
        self.in_city.delete(0, END)
        self.in_city.insert(0, first_item[10])  # City
        self.in_pos.delete(0, END)
        self.in_pos.insert(0, first_item[11])  # Job Position
        self.in_salary.delete(0, END)
        self.in_salary.insert(0, first_item[12])  # Salary
        self.in_turn.delete(0, END)
        self.in_turn.insert(0, first_item[13])  # Work Shift 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def run(self): # metodo para rodar o loop do form

        self.rhroot.mainloop() # loop do form

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
RHScreen()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

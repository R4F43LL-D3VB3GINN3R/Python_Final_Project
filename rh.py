#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from tkinter import *          # importa a biblioteca tkinter
from tkinter import ttk        # importa mais funcionalidades do tkinter
from database import Database  # importa a biblioteca de base de dados
from tkinter import messagebox # importa a caixa de mensagens do tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class RHScreen(): # inicializa a classe RH
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):
  
        self.rhroot = Tk()         # o objeto recebe a raiz da aplicacao 
        self.database = Database() # instancia do banco de dados
        self.rh_mainscreen()       # invoca o metodo de criacao e configuracao da tela de login
        self.rh_frame()            # invoca o metodo de criacao e configuracao do frame de tela
        self.rh_widgets()          # invoca o metodo de criacao e configuracao de widgets

        #---------------------

        self.rhroot.mainloop() # Loop temporário
    
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
        
    def rh_frame(self): # configuracao do frame de tela principal

        self.frame1 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame1.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=1)                                    # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def rh_widgets(self): # insercao de widgets de tela principal

        # Botões do Frame1
        self.bt_insert = Button(self.frame1, text='Insert', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_insert) # setup 
        self.bt_insert.place(relx=0.01, rely=0.01, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_remove = Button(self.frame1, text='Search', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_search) # setup 
        self.bt_remove.place(relx=0.01, rely=0.09, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_paycheck = Button(self.frame1, text='Paycheck', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_paycheck) # setup 
        self.bt_paycheck.place(relx=0.01, rely=0.17, relwidth=1, relheight=0.07)                                                                                                                            # posicao
        
        self.bt_exitmenu = Button(self.frame1, text='Exit', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.rhroot.destroy) # setup 
        self.bt_exitmenu.place(relx=0.01, rely=0.25, relwidth=1, relheight=0.07)                                                                                                                        # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def validate_fields(self, field, data_type, length, field_name): # método de verificacao de campos

        field_value = field.get() if hasattr(field, 'get') else str(field)

        # Verificar se o campo contém as especificacoes desejadas
        if data_type == 'text' and field_name == 'Name':
            if not field_value.replace(" ", "").isalpha() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is text and has less than or equal to {length} characters.")
                return False
        elif data_type == 'alphanumeric' and field_name == 'IDC':
            if not field_value.replace(" ", "").isalnum() or len(field_value) > length: # Remover espaços e verificar se o restante é alfanumérico
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is alphanumeric and has less than or equal to {length} characters.")
                return False
        elif field_name == 'Sex' and field_value.lower() not in ['male', 'female']:
            messagebox.showerror("Error", f"{field_name} invalid. Please select 'Male' or 'Female'.")
            return False
        elif field_name == 'Age' and (not field_value.isdigit() or not 18 <= int(field_value) <= 99):
            messagebox.showerror("Error", f"{field_name} invalid. Please enter a numeric value between 18 and 99.")
            return False
        elif data_type == 'alphanumeric' and field_name == 'Address':
            if not field_value.replace(" ", "").isalnum() or len(field_value) > length: # Remover espaços e verificar se o restante é alfanumérico
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is alphanumeric and has less than or equal to {length} characters.")
                return False
        elif data_type == 'numeric' and field_name == 'Salary':
            if not field_value.isdigit() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is numeric and has less then {length} digits.")
                return False
        if data_type == 'numeric' and field_name == 'Phone':
            if not field_value.isdigit() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is numeric and has less then {length} digits.")
                return False
        elif data_type == 'text' and field_name == 'Nationality':
            if not field_value.replace(" ", "").isalpha() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is text and has less than or equal to {length} characters.")
                return False
        elif data_type == 'text' and field_name == 'City':
            if not field_value.replace(" ", "").isalpha() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is text and has less than or equal to {length} characters.")
                return False
        elif data_type == 'text' and field_name == 'Job':
            if not field_value.replace(" ", "").isalpha() or len(field_value) > length:
                messagebox.showerror("Error", f"{field_name} invalid. Make sure it is text and has less than or equal to {length} characters.")
                return False
        elif field_name == 'Marital' and field_value.lower() not in ['single', 'married', 'divorced', 'widower']:
            messagebox.showerror("Error", f"{field_name} invalid. Please select 'single', 'married', 'divorced' or 'widower'.")
            return False
        elif field_name == 'WorkShift' and field_value.lower() not in ['day', 'night']:
            messagebox.showerror("Error", f"{field_name} invalid. Please select 'day' or 'night'.")
            return False
        elif field_name == 'Dependents' and (not field_value.isdigit() or not 0 <= int(field_value) <= 20):
            messagebox.showerror("Error", f"{field_name} invalid. Please enter a valid numeric value")
            return False
        return True

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
        self.lb_age.place(relx=0.3, rely=0.22, relwidth=0.07, relheight=0.05)                                 # posicao

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

        self.in_id = Entry(self.frame2, bd=4, bg='grey')                      # setup
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
        self.bt_save_employee.place(relx=0.77, rely=0.8, relwidth=0.2, relheight=0.07)                                                                                                                       # posicao

        self.bt_clear_employee = Button(self.frame2, text='Clear', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.clear_fields) # setup 
        self.bt_clear_employee.place(relx=0.77, rely=0.9, relwidth=0.2, relheight=0.07)                                                                                                                       # posicao
                                                                                                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def show_employees(self):
         
        # Widgets 
        self.subframe2 = Toplevel(self.rhroot)
        self.subframe2.title("Employee Details")
        self.subframe2.geometry("1500x500")

        #--------------------------------------

        # Treeview
        self.listEmpl = ttk.Treeview(self.subframe2, height = 3, column = ("col0","col1", "col2'", "col3", "col4", "col5", "col6'", "col7", "col8", "col9", "col10'", "col11", "col12", "col13", "col14", "col15")) # objeto treeview criado na tela2
        self.insert_treeview() # método para exibir os dados dentro da treeview
        #--------------------------------------

        # Cabecalhos
        self.listEmpl.heading("#0", text="")                   # texto de cabecalho
        self.listEmpl.heading("#1", text="ID")                 # texto de cabecalho
        self.listEmpl.heading("#2", text="IDC")                # texto de cabecalho
        self.listEmpl.heading("#3", text="Name")               # texto de cabecalho.
        self.listEmpl.heading("#4", text="Age")                # texto de cabecalho
        self.listEmpl.heading("#5", text="Sex")                # texto de cabecalho
        self.listEmpl.heading("#6", text="Address")            # texto de cabecalho
        self.listEmpl.heading("#7", text="Phone")              # texto de cabecalho
        self.listEmpl.heading("#8", text="Marital Status")     # texto de cabecalho
        self.listEmpl.heading("#9", text="Dependents")         # texto de cabecalho
        self.listEmpl.heading("#10", text="Nationality")       # texto de cabecalho
        self.listEmpl.heading("#11", text="City")              # texto de cabecalho
        self.listEmpl.heading("#12", text="Job Position")      # texto de cabecalho
        self.listEmpl.heading("#13", text="Salary")            # texto de cabecalho
        self.listEmpl.heading("#14", text="Work Shift")        # texto de cabecalho
        self.listEmpl.heading("#15", text="Payment Situation") # texto de cabecalho

        #--------------------------------------

        # Colunas
        self.listEmpl.column("#0", width=10)    # tamanho da coluna
        self.listEmpl.column("#1", width=50)    # tamanho da coluna
        self.listEmpl.column("#2", width=50)    # tamanho da coluna
        self.listEmpl.column("#3", width=150)   # tamanho da coluna
        self.listEmpl.column("#4", width=50)    # tamanho da coluna
        self.listEmpl.column("#5", width=50)    # tamanho da coluna
        self.listEmpl.column("#6", width=150)   # tamanho da coluna
        self.listEmpl.column("#7", width=50)    # tamanho da coluna
        self.listEmpl.column("#8", width=100)   # tamanho da coluna
        self.listEmpl.column("#9", width=50)    # tamanho da coluna
        self.listEmpl.column("#10", width=100)  # tamanho da coluna
        self.listEmpl.column("#11", width=100)  # tamanho da coluna
        self.listEmpl.column("#12", width=100)  # tamanho da coluna
        self.listEmpl.column("#13", width=50)   # tamanho da coluna
        self.listEmpl.column("#14", width=120)  # tamanho da coluna
        self.listEmpl.column("#15", width=120)  # tamanho da coluna

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
        self.turn = self.in_turn.get()               # objeto criado recebe o que for digitado na entrada
        self.pay = 'No'                              # objeto criado recebe a string

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def insert_client(self): # metodo para inserir o cliente na tabela.
        
        self.get_client()         # invoca o metodo para receber os dados inseridos na entrada
        self.database.open_conn() # abre a conexao com a base de dados
        
        if not self.validate_fields(self.in_name, 'text', 50, 'Name'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_idc, 'alphanumeric', 12, 'IDC'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_sex, 'text', 6, 'Sex'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_age, 'numeric', 2, 'Age'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_address, 'alphanumeric', 100, 'Address'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_phone, 'numeric', 7, 'Phone'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_marital, 'text', 9, 'Marital'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_nationality, 'text', 32, 'Nationality'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_sons, 'numeric', 1, 'Dependents'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código

        if not self.validate_fields(self.in_city, 'text', 49, 'City'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_pos, 'text', 20, 'Job'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_salary, 'numeric', 20, 'Salary'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código
        
        if not self.validate_fields(self.in_turn, 'text', 5, 'WorkShift'): # invoca o método de validacao de campos
            return # A validação falhou, não prossiga com o restante do código

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

            self.database.cursor.execute(
                """UPDATE tab_payment
                SET name = ? WHERE IDC = ?""",
                (self.name, self.idc)
            )
            messagebox.showinfo("Info", "Employee with IDC {} updated.".format(self.idc))
        else:
            # Empregado não existe, proceda com a inserção
            self.database.cursor.execute(
                """INSERT INTO tab_employees (IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (self.idc, self.name, self.age, self.sex, self.address, self.phone, self.marital, self.sons, self.nationality,
                self.city, self.pos, self.salary, self.turn, self.pay)
            )

            self.database.cursor.execute(
                """INSERT INTO tab_payment (IDC, name)
                VALUES (?, ?)""",
                (self.idc, self.name))
            messagebox.showinfo("Info", "Employee with IDC {} added.".format(self.idc))

        self.database.conn.commit() # executa a query SQL
        self.database.close_conn()  # encerra a conexao
        self.insert_treeview()      # invoca o método para povoar a treeview
        self.clear_fields()         # invoca o metodo para limpar os campos

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
         
    def insert_treeview(self): # método para inserir os dados das entradas na treeview

        self.listEmpl.delete(*self.listEmpl.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren

        self.database.open_conn() # abre conexão com banco de dados

        lista = self.database.cursor.execute(""" SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation FROM tab_employees ORDER BY name ASC; """)
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
            self.bt_show_employee.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.07)                                                                                                                                  # posicao
            
            #--------------------------------------                                                                                                                       
            
            # Treeview
            self.listEmplSearch = ttk.Treeview(self.frame3, height = 3, column = ("col0","col1", "col2'", "col3", "col4", "col5", "col6'", "col7", "col8", "col9", "col10'", "col11", "col12", "col13", "col14", "col15")) # objeto treeview criado na tela
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
            self.listEmplSearch.heading("#15", text="Pay Situation") # texto de cabecalho

            #--------------------------------------

            # Colunas
            self.listEmplSearch.column("#0", width=0)    # tamanho da coluna
            self.listEmplSearch.column("#1", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#2", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#3", width=150)  # tamanho da coluna
            self.listEmplSearch.column("#4", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#5", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#6", width=100)  # tamanho da coluna
            self.listEmplSearch.column("#7", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#8", width=100)  # tamanho da coluna
            self.listEmplSearch.column("#9", width=50)   # tamanho da coluna
            self.listEmplSearch.column("#10", width=100) # tamanho da coluna
            self.listEmplSearch.column("#11", width=100) # tamanho da coluna
            self.listEmplSearch.column("#12", width=100) # tamanho da coluna
            self.listEmplSearch.column("#13", width=50)  # tamanho da coluna
            self.listEmplSearch.column("#14", width=125) # tamanho da coluna
            self.listEmplSearch.column("#15", width=125) # tamanho da coluna

            #--------------------------------------

            # Treeview Configuracoes
            self.listEmplSearch.place(relx = 0.02, rely = 0.35, relwidth = 0.95, relheight = 0.4) # insere a treeview com posicao e tamanho desejado

            hsb = ttk.Scrollbar(self.frame3, orient="horizontal", command=self.listEmplSearch.xview)
            hsb.place(relx=0.02, rely=0.7, relwidth=0.94) # Posiciona a barra de rolagem horizontal

            self.listEmplSearch.configure(xscrollcommand=hsb.set) # Configura o comando de rolagem horizontal
                                                                                                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            
    def insert_treeview_search(self):
        
        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # Limpa os itens existentes na Treeview
        
        nome = self.in_namesearch.get() if self.in_namesearch.get() else '%' # Se a entrada de nome estiver vazia, use '%'

        self.database.open_conn() # Conecta ao banco de dados

        if self.in_idsearch.get(): # Executa a consulta com base no ID ou no nome
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift, pay_situation
                FROM tab_employees
                WHERE ID = ?""",
                (self.in_idsearch.get(),)
            ).fetchall() # Busca apenas pelo ID se fornecido
            if lista:
                self.bt_remove = Button(self.frame3, text='Remove', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.remove_employee)
                self.bt_remove.place(relx=0.03, rely=0.91, relwidth=0.2, relheight=0.06)
                self.bt_change = Button(self.frame3, text='Change', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.changebutton)
                self.bt_change.place(relx=0.03, rely=0.84, relwidth=0.2, relheight=0.06)
                self.bt_rgpd_remove = Button(self.frame3, text='RGPD Delete', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.remove_employee2)
                self.bt_rgpd_remove.place(relx=0.03, rely=0.77, relwidth=0.2, relheight=0.06)
                self.bt_show = Button(self.frame3, text='Show', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_employees)
                self.bt_show.place(relx=0.77, rely=0.82, relwidth=0.2, relheight=0.07)
                self.bt_removed = Button(self.frame3, text='Deleted', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_exemployees)
                self.bt_removed.place(relx=0.77, rely=0.9, relwidth=0.2, relheight=0.07)
                self.in_namesearch.delete(0, END)
                
        else: # Busca pelo ID ou pelo nome com correspondência parcial
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift, pay_situation
                FROM tab_employees
                WHERE ID = ? OR name LIKE ?""",
                (self.in_idsearch.get(), f'%{nome}%')
            ).fetchall()
            if lista:
                self.bt_remove = Button(self.frame3, text='Remove', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.remove_employee)
                self.bt_remove.place(relx=0.03, rely=0.91, relwidth=0.2, relheight=0.06)
                self.bt_change = Button(self.frame3, text='Change', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.changebutton)
                self.bt_change.place(relx=0.03, rely=0.84, relwidth=0.2, relheight=0.06)
                self.bt_rgpd_remove = Button(self.frame3, text='RGPD Delete', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.remove_employee2)
                self.bt_rgpd_remove.place(relx=0.03, rely=0.77, relwidth=0.2, relheight=0.06)
                self.bt_show = Button(self.frame3, text='Show', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_employees)
                self.bt_show.place(relx=0.77, rely=0.82, relwidth=0.2, relheight=0.07)
                self.bt_removed = Button(self.frame3, text='Deleted', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_exemployees)
                self.bt_removed.place(relx=0.77, rely=0.9, relwidth=0.2, relheight=0.07)
        
        for i in lista: # ciclo for para correr a pesquisa
            self.listEmplSearch.insert("", END, values=i) # insere cada item achado da pesquisa na lista

        if not lista or (self.in_idsearch.get() == '' and self.in_namesearch.get() == ''): # Exibe uma mensagem se nenhum registro for encontrado
            messagebox.showinfo("Info", "No records found for the search criteria.")
            self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # Limpa os itens existentes na Treeview
            self.in_namesearch.delete(0, END)

        self.database.close_conn() # Fecha a conexão com o banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def changebutton(self): # método do botâo change guarda dois métodos

        self.frame_insert()   # método para chamar a tela de cadastro de funcionários
        self.insert_entries() # método para transportar os dados da Treeview para as entradas da tela de cadastro de funcionários

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
         
    def insert_entries(self): # método para inserir os dados das entradas na treeview
     
        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren

        nome = self.in_namesearch.get()       # o nome recebe a entrada do nome
        id_to_search = self.in_idsearch.get() # o id recebe a entrada do id

        self.database.open_conn() # abre conexão com banco de dados

        if id_to_search:
            # Busca pelo ID
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift
                FROM tab_employees
                WHERE ID = ?""",
                (id_to_search,)
            ).fetchall()
        else:
            # Busca pelo nome
            lista = self.database.cursor.execute(
                """SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents,
                        nationality, city, job_position, salary, work_shift
                FROM tab_employees
                WHERE name LIKE ?""",
                (f'%{nome}%',)
            ).fetchall()

        if lista:
            for i in lista:
                self.listEmplSearch.insert("", END, values=i)

            first_item = lista[0]

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
        
    def remove_employee(self): # método para remover um funcionário da lista de funcionários

        nome = self.in_namesearch.get() # variável recebe a entrada do nome
        self.database.open_conn() # abre conexão com banco de dados

        if self.in_idsearch.get(): # Se houver um ID inserido
            self.database.cursor.execute( # insere o funcionário na tabela de ex-funcionários 
            """INSERT INTO tab_exemployees (ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation)
               SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation
               FROM tab_employees
               WHERE ID = ?""",
            (self.in_idsearch.get(),))

            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no ID
                """DELETE FROM tab_employees WHERE ID = ?""",
                (self.in_idsearch.get(),))
            
            self.database.cursor.execute( # remove o funcionário da tabela pagamentos baseado no ID
                """DELETE FROM tab_payment WHERE ID = ?""",
                (self.in_idsearch.get(),))
            
            self.database.cursor.execute( # insere a chave removida para evitar erros de duplicacâo de chaves
                """INSERT INTO tab_employees (ID) 
                VALUES (?)""",
                (self.in_idsearch.get(),))
        else: # do contrário...
            self.database.cursor.execute( # insere o funcionário na tabela de ex-funcionários 
            """INSERT INTO tab_exemployees (ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation)
               SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation
               FROM tab_employees
               WHERE name LIKE ?""",
            (f'%{nome}%',))

            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no Nome
                """DELETE FROM tab_employees WHERE name LIKE ?""",
                (f'%{nome}%',))
            
            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no Nome
                """DELETE FROM tab_payment WHERE name LIKE ?""",
                (f'%{nome}%',))
            
            self.database.cursor.execute( # insere a chave removida para evitar erros de duplicacâo de chaves
                """INSERT INTO tab_employees (ID) 
                VALUES (?)""",
                (self.in_idsearch.get(),))

        self.database.conn.commit()  # Confirmar a operação de DELETE
        self.database.close_conn()   # Fechar a conexão com o banco de dados

        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren
        messagebox.showinfo("Info", "Employee removed") # exibe a mensagem

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def remove_employee2(self): # método para remover um funcionário da lista de funcionários

        nome = self.in_namesearch.get() # variável recebe a entrada do nome
        self.database.open_conn() # abre conexão com banco de dados

        if self.in_idsearch.get(): # Se houver um ID inserido
            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no ID
                """DELETE FROM tab_employees WHERE ID = ?""",
                (self.in_idsearch.get(),))
            
            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no ID
                """DELETE FROM tab_payment WHERE ID = ?""",
                (self.in_idsearch.get(),))
        else: # do contrário...
            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no Nome
                """DELETE FROM tab_employees WHERE name LIKE ?""",
                (f'%{nome}%',))
            
            self.database.cursor.execute( # remove o funcionário da tabela de funcionários baseado no Nome
                """DELETE FROM tab_payment WHERE name LIKE ?""",
                (f'%{nome}%',))

        self.database.conn.commit()  # Confirmar a operação de DELETE
        self.database.close_conn()   # Fechar a conexão com o banco de dados

        self.listEmplSearch.delete(*self.listEmplSearch.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren
        messagebox.showinfo("Info", "Employee removed") # exibe a mensagem
        
    def show_exemployees(self):
         
        # Widgets 
        self.subframe2 = Toplevel(self.rhroot)
        self.subframe2.title("Employee Details")
        self.subframe2.geometry("1500x500")

        #--------------------------------------

        # Treeview
        self.listEmpl = ttk.Treeview(self.subframe2, height = 3, column = ("col0","col1", "col2'", "col3", "col4", "col5", "col6'", "col7", "col8", "col9", "col10'", "col11", "col12", "col13", "col14", "col15")) # objeto treeview criado na tela2
        self.insert_treeview2() # método para exibir os dados dentro da treeview
        #--------------------------------------

        # Cabecalhos
        self.listEmpl.heading("#0", text="")                   # texto de cabecalho
        self.listEmpl.heading("#1", text="ID")                 # texto de cabecalho
        self.listEmpl.heading("#2", text="IDC")                # texto de cabecalho
        self.listEmpl.heading("#3", text="Name")               # texto de cabecalho
        self.listEmpl.heading("#4", text="Age")                # texto de cabecalho
        self.listEmpl.heading("#5", text="Sex")                # texto de cabecalho
        self.listEmpl.heading("#6", text="Address")            # texto de cabecalho
        self.listEmpl.heading("#7", text="Phone")              # texto de cabecalho
        self.listEmpl.heading("#8", text="Marital Status")     # texto de cabecalho
        self.listEmpl.heading("#9", text="Dependents")         # texto de cabecalho
        self.listEmpl.heading("#10", text="Nationality")       # texto de cabecalho
        self.listEmpl.heading("#11", text="City")              # texto de cabecalho
        self.listEmpl.heading("#12", text="Job Position")      # texto de cabecalho
        self.listEmpl.heading("#13", text="Salary")            # texto de cabecalho
        self.listEmpl.heading("#14", text="Work Shift")        # texto de cabecalho
        self.listEmpl.heading("#15", text="Payment Situation") # texto de cabecalho

        #--------------------------------------

        # Colunas
        self.listEmpl.column("#0", width=10)    # tamanho da coluna
        self.listEmpl.column("#1", width=50)    # tamanho da coluna
        self.listEmpl.column("#2", width=50)    # tamanho da coluna
        self.listEmpl.column("#3", width=150)   # tamanho da coluna
        self.listEmpl.column("#4", width=50)    # tamanho da coluna
        self.listEmpl.column("#5", width=50)    # tamanho da coluna
        self.listEmpl.column("#6", width=150)   # tamanho da coluna
        self.listEmpl.column("#7", width=50)    # tamanho da coluna
        self.listEmpl.column("#8", width=100)   # tamanho da coluna
        self.listEmpl.column("#9", width=50)    # tamanho da coluna
        self.listEmpl.column("#10", width=100)  # tamanho da coluna
        self.listEmpl.column("#11", width=100)  # tamanho da coluna
        self.listEmpl.column("#12", width=100)  # tamanho da coluna
        self.listEmpl.column("#13", width=50)   # tamanho da coluna
        self.listEmpl.column("#14", width=125)  # tamanho da coluna
        self.listEmpl.column("#15", width=125)  # tamanho da coluna

        #--------------------------------------

        # Treeview Configuracoes
        self.listEmpl.place(relx = 0.01, rely = 0.05, relwidth = 0.95, relheight = 0.85)    # insere a treeview com posicao e tamanho desejado

        vsb = ttk.Scrollbar(self.subframe2, orient="vertical", command=self.listEmpl.yview) # objeto barra de rolagem criado na tela2
        vsb.place(relx = 0.96, rely = 0.05, relheight = 0.85)                               # insere a barra de rolagem com posicao e tamanho desejado
        self.listEmpl.configure(yscrollcommand=vsb.set)                                     # configuracao da barra de rolagem

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def insert_treeview2(self): # método para inserir os dados das entradas na treeview
    
        self.listEmpl.delete(*self.listEmpl.get_children()) # o objeto deleta os elementos desempacotados da lista por getchildren

        self.database.open_conn() # abre conexão com banco de dados

        lista = self.database.cursor.execute(""" SELECT ID, IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift, pay_situation FROM tab_exemployees ORDER BY name ASC; """)
        # seleciona todos os campos da tabela na lista e os ordena pelos nomes dos empregados em ordem alfabetica

        for i in lista:                              # percorre todos os itens da lista que guarda os resultados da consulta ao banco de dados 
             self.listEmpl.insert("", END, values=i) # os itens serão inseridos a lista do topo ao final

        self.database.close_conn() # fecha conexão com o banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def frame_paycheck(self):

        # Tela Principal 

        self.frame4 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame4.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                      # posicao

        #--------------------------------------

        # Widgets - [Molduras] 

        self.canvas_frame4 = Canvas(self.frame4, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas_frame4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)                                                 # posiciona a moldura 

        self.canvas2_frame4 = Canvas(self.frame4, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas2_frame4.place(relx=0.01, rely=0.33, relwidth=0.48, relheight=0.27)                                                # posiciona a moldura    

        self.canvas3_frame4 = Canvas(self.frame4, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas3_frame4.place(relx=0.01, rely=0.9, relwidth=0.98, relheight=0.09)                                                # posiciona a moldura   

        self.canvas4_frame4 = Canvas(self.frame4, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas4_frame4.place(relx=0.51, rely=0.33, relwidth=0.48, relheight=0.27)                                                # posiciona a moldura    

        self.canvas5_frame4 = Canvas(self.frame4, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
        self.canvas5_frame4.place(relx=0.01, rely=0.62, relwidth=0.98, relheight=0.12)                                                # posiciona a moldura    

        #--------------------------------------

        # Widgets - [Labels] 

        # Canvas 1 ----------------------------
    
        self.lb_title4 = Label(self.frame4, text = 'Search Employee', bg='grey', font=('comic-sans', 15, 'bold', 'italic')) # setup
        self.lb_title4.place(relx=0.28, rely=0.03, relwidth=0.4, relheight=0.05)                                            # posicao

        self.lb_id4 = Label(self.frame4, text = 'ID:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_id4.place(relx=0.09, rely=0.1, relwidth=0.04, relheight=0.05)                                # posicao

        self.lb_name4 = Label(self.frame4, text = 'Name:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
        self.lb_name4.place(relx=0.24, rely=0.1, relwidth=0.1, relheight=0.05)                                   # posicao

        # Canvas 2 ----------------------------

        self.lb_brutesal4 = Label(self.frame4, text = 'Brute Salary:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_brutesal4.place(relx=0.07, rely=0.35, relwidth=0.2, relheight=0.05)                                          # posicao 

        self.lb_liqsal4 = Label(self.frame4, text = 'Liquid Salary:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_liqsal4.place(relx=0.07, rely=0.41, relwidth=0.2, relheight=0.05)                                           # posicao 

        self.lb_extrahour4 = Label(self.frame4, text = 'Extra - Hours:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_extrahour4.place(relx=0.07, rely=0.47, relwidth=0.2, relheight=0.05)                                           # posicao 

        self.lb_nopayleave4 = Label(self.frame4, text = 'Nopay Leave:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_nopayleave4.place(relx=0.07, rely=0.53, relwidth=0.2, relheight=0.05)                                         # posicao 

        # Canvas 4 ----------------------------

        self.lb_healthplan4 = Label(self.frame4, text = 'Health Plan:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_healthplan4.place(relx=0.6, rely=0.35, relwidth=0.17, relheight=0.05)                                        # posicao 

        self.lb_ticketrans4 = Label(self.frame4, text = 'Transport Ticket:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_ticketrans4.place(relx=0.6, rely=0.41, relwidth=0.24, relheight=0.05)                                              # posicao 

        self.lb_foodticket4 = Label(self.frame4, text = 'Food Ticket:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_foodticket4.place(relx=0.6, rely=0.47, relwidth=0.17, relheight=0.05)                                         # posicao 

        self.lb_sindical_contr4 = Label(self.frame4, text = 'Sindical Contr:', bg='grey', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.lb_sindical_contr4.place(relx=0.59, rely=0.53, relwidth=0.22, relheight=0.05)                                           # posicao 

        #--------------------------------------  

        # Widgets - [Entradas] 

        # Canvas 1 ----------------------------

        self.in_idsearch4 = Entry(self.frame4, bd=4)                               # setup
        self.in_idsearch4.place(relx=0.14, rely=0.1, relwidth=0.1, relheight=0.05) # posicao

        self.in_namesearch4 = Entry(self.frame4, bd=4, bg='grey')                    # setup
        self.in_namesearch4.place(relx=0.34, rely=0.1, relwidth=0.6, relheight=0.05) # posicao

        # Canvas 2 ----------------------------

        self.in_brutesal4 = Entry(self.frame4, bd=4)                                 # setup
        self.in_brutesal4.place(relx=0.28, rely=0.35, relwidth=0.12, relheight=0.05) # posicao

        self.in_liqsal4 = Entry(self.frame4, bd=4)                                 # setup
        self.in_liqsal4.place(relx=0.28, rely=0.41, relwidth=0.12, relheight=0.05) # posicao

        self.in_extrahour4 = Entry(self.frame4, bd=4)                                 # setup
        self.in_extrahour4.place(relx=0.28, rely=0.47, relwidth=0.12, relheight=0.05) # posicao

        self.in_nopayleave4 = Entry(self.frame4, bd=4)                                 # setup
        self.in_nopayleave4.place(relx=0.28, rely=0.53, relwidth=0.12, relheight=0.05) # posicao

        # Canvas 3 ----------------------------

        self.in_sal4 = Entry(self.frame4, bd=4)                                 # setup
        self.in_sal4.place(relx=0.85, rely=0.92, relwidth=0.12, relheight=0.05) # posicao

        # Widgets - [Botões] 

        # Canvas 1 ----------------------------

        self.bt_show_employee4 = Button(self.frame4, text='Start', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.show_employee_salary) # setup 
        self.bt_show_employee4.place(relx=0.39, rely=0.2, relwidth=0.2, relheight=0.07)                                                                                                                               # posicao
        
        # Canvas 5 ----------------------------                                                                                                                          

        self.bt_refresh4 = Button(self.frame4, text='Refresh', bd=5, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.calculate_sal) # setup 
        self.bt_refresh4.place(relx=0.37, rely=0.65, relwidth=0.25, relheight=0.06)                                                                                                                        # posicao
        

        self.bt_gensal4 = Button(self.frame4, text='Generate', bd=4, bg='white', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic')) # setup 
        self.bt_gensal4.place(relx=0.65, rely=0.92, relwidth=0.2, relheight=0.06)                                                                                              # posicao

        #--------------------------------------

        # Widgets - [Checkboxes]

        # Canvas 4 ----------------------------    

        self.healthplan_var = BooleanVar()     # variável boleana para checkbutton
        self.ticketrans_var = BooleanVar()     # variável boleana para checkbutton
        self.foodticket_var = BooleanVar()     # variável boleana para checkbutton
        self.sindical_contr_var = BooleanVar() # variável boleana para checkbutton

        self.cb_healthplan4 = Checkbutton(self.frame4, bg='grey', variable=self.healthplan_var) # setup
        self.cb_healthplan4.place(relx=0.86, rely=0.35, relwidth=0.04, relheight=0.06)          # posicao

        self.cb_ticketrans4 = Checkbutton(self.frame4, bg='grey', variable=self.ticketrans_var) # setup
        self.cb_ticketrans4.place(relx=0.86, rely=0.41, relwidth=0.04, relheight=0.06)          # posicao

        self.cb_foodticket4 = Checkbutton(self.frame4, bg='grey', variable=self.foodticket_var) # setup
        self.cb_foodticket4.place(relx=0.86, rely=0.47, relwidth=0.04, relheight=0.06)          # posicao

        self.cb_sindical_contr4 = Checkbutton(self.frame4, bg='grey', variable=self.sindical_contr_var) # setup
        self.cb_sindical_contr4.place(relx=0.86, rely=0.53, relwidth=0.04, relheight=0.06)              # posicao
  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def show_employee_salary(self): # método para capturar o salário de um funcionário e inseri-lo em outra entrada

        employee_id = self.in_idsearch4.get()  # obter o ID da entrada

        if not employee_id: # se os campos estiverem vazios...
            messagebox.showinfo("Info", "Please enter ID.") # exibe a mensagem
            return # ignora o resto do codigo

        self.database.open_conn() # abre conexão com a base de dados

        existing_employee = self.database.cursor.execute(
            """SELECT salary, name FROM tab_employees WHERE ID = ?""",
            (employee_id,)
        ).fetchone() # executa a consulta para obter o salário do funcionário
        
        if existing_employee and existing_employee[0] and existing_employee[1] is not None:    # se houver um funcionário com salário associado...
            salary = existing_employee[0]                                                      # guarda o valor do salário na variável
            employee_name = existing_employee[1]                                               # Obtém o nome do funcionário
            self.in_namesearch4.delete(0, 'end')                                               # deleta o nome recém inserido na entrada
            self.in_namesearch4.insert(0, str(employee_name))                                  # insere o valor da variável na entrada
            self.in_sal4.delete(0, 'end')                                                      # limpar qualquer conteúdo anterior
            self.in_sal4.insert(0, str(salary))                                                # insere o valor da variável na entrada
        else:                                                                                  # do contrário...
            messagebox.showinfo("Info", f"No salary found for employee with ID {employee_id}") # exibe mensagem
            self.in_namesearch4.delete(0, 'end')                                               # deleta o nome recém inserido na entrada
            self.in_sal4.delete(0, 'end')                                                      # limpar qualquer conteúdo anterior

        self.database.close_conn() # fecha conexão com a base de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def calculate_sal(self): # método para calcular o salário do funcionário

        # Variáveis de Trabalho 

        self.lv_sal = 0.0         # salário base
        self.lv_brutesal = 0.0    # salário bruto
        self.lv_liqsal = 0.0      # salário líquido

        self.lv_extrahour = 0.0   # horas extras
        self.lv_nopayleave = 0.0  # horas de falta

        self.lv_secsocial = 0.0   # seguranca social
        self.lv_irs = 0.0         # imposto de renda
        self.lv_subdec = 0.0      # subsídio décimo terceiro

        self.lv_deductions = 0.0  # deducoes totais
        self.lv_salbonus = 0.0    # bonus total

        #--------------------------------------------------------------------------------

        # Validação de Campos [Futuramente um Método para isto]

        employee_id = self.in_idsearch4.get() # variável recebe o id da entrada
        self.lv_sal = self.in_sal4.get()      # variável recebe o salário da entrada

        if not employee_id: # se os campos estiverem vazios...
            messagebox.showinfo("Info", "Please enter a valid ID.") # exibe a mensagem
            return # ignora o resto do codigo
        
        if not self.lv_sal: # se os campos estiverem vazios...
            messagebox.showinfo("Info", "No Salary to Calculate") # exibe a mensagem
            return # ignora o resto do codigo
        
        #---------------------------------------------------------------------------------
        
        # Adicional Noturno [Bônus Salarial + 25%]

        self.database.open_conn() # abre conexão com a base de dados

        work_shift_vf = self.database.cursor.execute(
            """SELECT work_shift FROM tab_employees WHERE ID = ?""",
            (employee_id,)
        ).fetchone() # executa a consulta para obter o turno do funcionário

        if work_shift_vf[0] == 'Day': # se o turno for dia...
            self.lv_salbonus = 0 # nao há adicional noturno
        else: # do contrario...
            self.lv_salbonus = float(self.lv_sal) * 0.25 # bonus salarial recebe 25% do ordenado base
        self.database.close_conn() # encerra conexao com base de dados

        #---------------------------------------------------------------------------------

        # Horas Extras [Valor da Hora = Salário / ( 8 horas trabalhadas * 22 dias úteis do mês)]

        self.lv_extrahour = self.in_extrahour4.get() # variável recebe a quantidade de horas extras trabalhadas
        self.lv_valhora = float(self.lv_sal) / (8 * 22) # valor da hora trabalhada

        if not self.lv_extrahour:
            self.lv_extrahour = 0.0
        else:
            if work_shift_vf[0] == 'Day': # se o turno for dia...
                self.lv_valhora = self.lv_valhora * 2 # dobra o valor da hora extra
            else: # do contrario...
                self.lv_valhora = self.lv_valhora * 3 # triplica o valor da hora extra

        self.lv_totalhours = round(float(self.lv_extrahour) * self.lv_valhora, 2) # O valor total recebe a quantidade de horas vezes o valor das horas extras
        self.lv_brutesal = round(float(self.lv_sal) + self.lv_totalhours, 2) # o salário bruto recebe o salário base + o valor total das horas extras

        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------

        # Subsídio Décimo [subsídio décimo/ férias = salário bruto / 12 + salário / 12]

        self.lv_subdec = round(self.lv_subdec + ((self.lv_brutesal / 12) + (float(self.lv_sal) / 12)), 2) # alimenta a variável de décimo e férias
        self.lv_salbonus = self.lv_salbonus + self.lv_subdec # acrescenta o subsídio décimo e férias ao bônus salarial

        #---------------------------------------------------------------------------------

        # Serviços [plano de saúde/ contribuição sindical/ vale transporte / vale refeicao]

        # [PLANO DE SAÚDE]

        if self.healthplan_var.get(): # se houver plano de saúde...
            self.healthplan2 = True # variável boleana recebe True
            self.lv_deductions = self.lv_deductions + 40 # as deducoes recebem o valor do preco do plano
        else: # do contrario...
            self.healthplan2 = False # variável boleana recebe False
        
        #---------------------------------------------------------------------------------
            
        # [VALE TRANSPORTE]
        
        if self.ticketrans_var.get(): # se houver plano de vale transporte...
            self.tickettrans2 = True # variável boleana recebe True
            self.lv_salbonus = self.lv_salbonus + 50 # os bonus recebem o valor do vale transporte
        else: # do contrário...
            self.tickettrans2 = False # a variavel boleana recebe False
        
        #---------------------------------------------------------------------------------

        # [VALE REFEICAO]

        if self.foodticket_var.get(): # se houver ticket refeicao
            self.foodticket2 = True # variável boleana recebe True
            self.lv_salbonus = self.lv_salbonus + 132 # os bonus recebem o valor do ticket alimentacao
        else: # do contrario
            self.foodticket2 = False # a variavel boleana recebe False

        #---------------------------------------------------------------------------------
        
        # [CONTRIBUICAO SINDICAL]

        if self.sindical_contr_var.get(): # se houver contribuicao sindical
            self.sindical2 = True # variável boleana recebe True
            self.lv_deductions = self.lv_deductions + 50 # os bonus recebem o valor do ticket alimentacao
        else: # do contrario
            self.sindical2 = False # a variavel boleana recebe False
            
        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------
            
        # Segurança Social
        
        if float(self.lv_sal) < 886:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
        elif float(self.lv_sal) >= 886 and float(self.lv_sal) < 932:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.06 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.06 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 932 and float(self.lv_sal) < 999:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.08 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.08 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 999 and float(self.lv_sal) < 1106:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.09 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.09 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 1106 and float(self.lv_sal) < 1600:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.11 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.11 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 1600 and float(self.lv_sal) < 1961:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.16 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.16 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 1961 and float(self.lv_sal) < 2529:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.19 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.19 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 2529 and float(self.lv_sal) < 3694:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.23 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.23 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 3694 and float(self.lv_sal) < 5469:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.28 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.28 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 5469 and float(self.lv_sal) < 6420:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.32 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.32 * float(self.lv_sal), 2)
        elif float(self.lv_sal) >= 6420 and float(self.lv_sal) < 20064:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.33 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.33 * float(self.lv_sal), 2)
        else:
            self.lv_deductions = self.lv_deductions + (0.11 * float(self.lv_sal) + (0.41 * float(self.lv_sal)))
            self.lv_secsocial = 0.11 * float(self.lv_sal)
            self.lv_irs = round(0.41 * float(self.lv_sal), 2)

        #--------------------------------------------------------------------------------

        # Nopay Leave 
            
        self.lv_nopayleave = self.in_nopayleave4.get() # variável recebe a quantidade de horas extras trabalhadas
        self.lv_valhora2 = float(self.lv_sal) / (8 * 22) # valor da hora trabalhada

        if not self.lv_nopayleave: # se não houverem faltas do funcionário
            self.lv_nopayleave = 0.0 # a variável recebe 0
        else: # do contrario...
            if work_shift_vf[0] == 'Day': # se o turno for dia...
                self.lv_valhora2 = self.lv_valhora2 * 2 # dobra o valor da hora extra
            else: # do contrario...
                self.lv_valhora2 = self.lv_valhora2 * 3 # triplica o valor da hora extra

        self.lv_totalhours2 = round(float(self.lv_nopayleave) * self.lv_valhora2, 2) # O valor total recebe a quantidade de horas vezes o valor das horas extras
        self.lv_deductions = round(self.lv_deductions + self.lv_totalhours2, 2) # as deducoes recebem o valor das horas faltadas de trabalho

        #---------------------------------------------------------------------------------

        # Deductions & Bonus

        self.lv_liqsal = self.lv_brutesal - self.lv_deductions + self.lv_salbonus # valor final do salário líquido

        print(f"Employee ID: {employee_id}")
        print(f"Employee Name: {self.in_namesearch4.get()}")
        print(f"Brute Salary: {self.lv_brutesal}")
        print(f"Liquid Salary: {self.lv_liqsal}")
        print(f"Health Plan: {self.healthplan2}")
        print(f"Contr Sindica: {self.sindical2}")
        print(f"Ticket Transport: {self.tickettrans2}")
        print(f"Food Ticket: {self.foodticket2}")
        print(f"Extra Hours: {self.lv_totalhours}")
        print(f"Deductions: {self.lv_deductions}")
        print(f"Social Security: {self.lv_secsocial}")
        print(f"IRS: {self.lv_irs}")
        print(f"Bonus Salary: {self.lv_salbonus}")
        print(f"Nopay Leave: {self.lv_totalhours2}")
        print(f"Subdec: {self.lv_subdec}")
        
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def run(self): # metodo para rodar o loop do form

        self.rhroot.mainloop() # loop do form

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
RHScreen()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

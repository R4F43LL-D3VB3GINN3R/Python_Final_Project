#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from tkinter import *          # importa a biblioteca tkinter
from tkinter import ttk        # importa mais funcionalidades do tkinter
from menu import MenuScreen    # importa a classe do menu
from database import Database  # importa a classe do banco de dados
import sqlite3                 # importa a biblioteca sqlite
from tkinter import messagebox # importa a caixa de mensagens do tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

root = Tk() # inicializa o tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Login(): # inicializa a classe Login
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self): # inicializa os objetos da classe ao invocá-la

        self.login = root          # o objeto recebe a raiz da aplicacao
        self.database = Database() # instancia do banco de dados
        self.login_screen()        # invoca o metodo de criacao e configuracao da tela de login
        self.login_frame()         # invoca o metodo de criacao e configuracao do frame de tela
        self.login_widgets()       # invoca o metodo de criacao e configuracao de widgets
        self.count = 3             # contador de tentativas de login
        root.mainloop()            # funcao para rodar o tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def login_screen(self): # configuracoes de tela

        self.login.title("Welcome")                                 # titulo 
        screen_width = self.login.winfo_screenwidth()               # coordenada da largura    
        screen_height = self.login.winfo_screenheight()             # coordenada da altura
        x_cordinate = int((screen_width/2) - (500/2))               # setup de posicao horizontal
        y_cordinate = int((screen_height/2) - (600/2))              # setup de posicao vertical
        self.login.geometry(f'500x600+{x_cordinate}+{y_cordinate}') # resolucao da tela e posicionamento dos setups
        self.login.configure(bg='white')                            # configuracao 
        self.login.configure(cursor='hand2')                        # cursor
        self.login.configure(takefocus=True)                        # foco
        self.login.configure(borderwidth=50, relief="groove")       # borda
        self.login.iconbitmap('icons/001 - login.ico')              # icon 
        self.login.resizable(True, True)                            # responsividade 
        self.login.maxsize(width=600, height=700)                   # tamanho maximo
        self.login.minsize(width=400, height=500)                   # tamanho minimo                 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def login_frame(self): # configuracao do frame de tela

        self.frame = Frame(self.login, bd = 4, bg='white', highlightbackground='grey', highlightthickness=3) # setup 
        self.frame.place(relx=0.001, rely=0.001, relwidth=1, relheight=1.01)                                 # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def login_widgets(self): # insercao de widgets

        # Botões
        self.bt_login = Button(self.login, text='Login', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.pressed_login) # setup 
        self.bt_login.place(relx=0.38, rely=0.8, relwidth=0.25, relheight=0.07)                                                                                                                     # posicao

        self.bt_exit = Button(self.login, text='Exit', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.login.destroy) # setup 
        self.bt_exit.place(relx=0.38, rely=0.9, relwidth=0.25, relheight=0.07)                                                                                                                    # posicao

        #--------------------------------------

        # Imagens
        self.avatar = PhotoImage(file='images/001 - login_avatar.png')             # diretório
        self.label_avatar = Label(self.login, image=self.avatar, bg='white')       # setup
        self.label_avatar.place(relx=0.21, rely=0.12, relwidth=0.6, relheight=0.5) # posicao

        self.id_image = PhotoImage(file='icons/002 - id.png')                         # diretório
        self.label_id_image = Label(self.login, image=self.id_image, bg='white')      # setup
        self.label_id_image.place(relx=0.7, rely=0.64, relwidth=0.1, relheight=0.061) # posicao

        self.pass_image = PhotoImage(file='icons/003 - pass.png')                        # diretório
        self.label_pass_image = Label(self.login, image=self.pass_image, bg='white')     # setup
        self.label_pass_image.place(relx=0.7, rely=0.73, relwidth=0.09, relheight=0.061) # posicao

        #--------------------------------------

        # Labels
        self.login_label = Label(self.login, text = 'Welcome', bg='white', font=('comic-sans', 20, 'bold', 'italic')) # setup
        self.login_label.place(relx=0.35, rely=0.017, relwidth=0.3, relheight=0.1)                                    # posicao

        self.id_label = Label(self.login, text = 'Username:', bg='white', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.id_label.place(relx=0.06, rely=0.63, relwidth=0.3, relheight=0.1)                                       # posicao

        self.login_label = Label(self.login, text = 'Password:', bg='white', font=('comic-sans', 12, 'bold', 'italic')) # setup
        self.login_label.place(relx=0.054, rely=0.7, relwidth=0.3, relheight=0.1)                                       # posicao

        #--------------------------------------

        # Entradas
        self.id = Entry(self.login, bd=4)                        # setup
        self.id.place(relx = 0.32, rely = 0.65, relwidth = 0.38) # posicao

        self.password = Entry(self.login, bd=4, show='*')              # setup
        self.password.place(relx = 0.32, rely = 0.73, relwidth = 0.38) # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def pressed_login(self): # método para verificar senha e login de usuário

        username = self.id.get()       # obtém a entrada do nome de usuário
        password = self.password.get() # obtém a entrada da senha

        if self.database.verify_user_credentials(username, password):                        # se credenciais usando o método do banco de dados for verdadeiro...
            self.login.destroy()                                                             # fecha a tela de login
            menu = MenuScreen()                                                              # cria uma instância do menu
            menu.run()                                                                       # roda a tela do menu
        elif username == "" and password == "":                                              # se os campos estiverem vazios...
            messagebox.showinfo("Aviso", "Preencha os campos.")                              # exibe pop-up com aviso                                         
            self.count -= 1                                                                  # decrementa o contador                                                                              
            self.try_login()                                                                 # chama a funcao para exibir as tentativas restantes
        elif username == "":                                                                 # se o campo estiver vazio
            messagebox.showinfo("Aviso", "Preencha o campo Username.")                       # exibe pop-up com aviso
            self.count -= 1                                                                  # decrementa o contador    
            self.try_login()                                                                 # chama a funcao para exibir as tentativas restantes
        elif password == "":                                                                 # se o campo estiver vazio
            messagebox.showinfo("Aviso", "Preencha o campo Password.")                       # exibe pop-up com aviso
            self.count -= 1                                                                  # chama a funcao para exibir as tentativas restantes
            self.try_login()                                                                 # do contrario...
        else:                                                                                # exibe pop-up com aviso de acesso negado
            messagebox.showwarning("Acesso Negado", "Credenciais inválidas. Acesso negado.") # exibe pop-up com aviso
            self.count -= 1                                                                  # decrementa o contador
            self.try_login()                                                                 # chama a funcao para exibir as tentativas restantes

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def try_login(self): # método para contar tentativas de login
 
        if self.count == 0:                                                                                                    # se o contador chegar a zero...
            messagebox.showwarning("Tentativas Restantes", "Você não possui mais tentativas")                                  # exibe pop-up com aviso
            messagebox.showwarning("Bloqueio de Programa Ativado", "Número de tentativas esgotado, o programa será encerrado") # exibe pop-up com aviso
            self.login.destroy()                                                                                               # fecha a tela de login
        elif self.count == 1:                                                                                                  # se o contador chegar a 1...
            messagebox.showwarning("Tentativas Restantes", "Você tem " + str(self.count) + " tentativa")                       # exibe pop-up com aviso
        elif self.count == 2:                                                                                                  # se o contador chegar a 2...
            messagebox.showwarning("Tentativas Restantes", "Você tem " + str(self.count) + " tentativas")                      # exibe pop-up com aviso
        elif self.count == 3:                                                                                                  # se o contador for 3...
            messagebox.showwarning("Tentativas Restantes", "Você tem " + str(self.count) + " tentativas")                      # exibe pop-up com aviso
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
        
Login() # chama a instancia da classe 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

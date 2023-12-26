#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from tkinter import *   # importa a biblioteca tkinter
from tkinter import ttk # importa mais funcionalidades do tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class MenuScreen(): # inicializa a classe menu
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):

        self.menuroot = Tk()
        self.menu_screen()
        self.menu_frame()
        self.menu_widgets()
        self.menuroot.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def menu_screen(self):

        self.menuroot.title("Menu")                                                       # título 
        screen_width = self.menuroot.winfo_screenwidth()                                  # coordenada da largura    
        screen_height = self.menuroot.winfo_screenheight()                                # coordenada da altura
        form_width = 800                                                                  # largura
        form_height = 600                                                                 # altura     
        x_cordinate = int((screen_width/2) - (form_width/2))                              # setup de posição horizontal
        y_cordinate = int((screen_height/2) - (form_height/2))                            # setup de posição vertical    
        self.menuroot.geometry(f'{form_width}x{form_height}+{x_cordinate}+{y_cordinate}') # resolução da tela e posicionamento dos setups
        self.menuroot.configure(bg='white')                                               # configuração 
        self.menuroot.configure(cursor='hand2')                                           # cursor
        self.menuroot.configure(takefocus=True)                                           # foco
        self.menuroot.configure(borderwidth=50, relief="groove")                          # borda
        self.menuroot.iconbitmap('icons/001 - login.ico')                                 # ícone 
        self.menuroot.resizable(True, True)                                               # responsividade 
        self.menuroot.maxsize(width=1200, height=800)                                     # tamanho máximo
        self.menuroot.minsize(width=600, height=400)                                      # tamanho mínimo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def menu_frame(self): # configuracao do frame de tela

        self.frame1 = Frame(self.menuroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame1.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=1)                                      # posicao

        self.frame2 = Frame(self.menuroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
        self.frame2.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                        # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def menu_widgets(self): # insercao de widgets

        # Botões
        self.bt_rh = Button(self.frame1, text='Human Resources', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic')) # setup 
        self.bt_rh.place(relx=0.01, rely=0.01, relwidth=1, relheight=0.07)                                                                                                      # posicao

        self.bt_exit = Button(self.frame1, text='Exit', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic')) # setup 
        self.bt_exit.place(relx=0.01, rely=0.9, relwidth=1, relheight=0.07)                                                                                            # posicao

        #--------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def run(self):

        self.menuroot.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
MenuScreen()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

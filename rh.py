#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from tkinter import *   # importa a biblioteca tkinter
from tkinter import ttk # importa mais funcionalidades do tkinter

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class RHScreen(): # inicializa a classe RH
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):
  
        self.rhroot = Tk()      # o objeto recebe a raiz da aplicacao 
        self.rh_screen()        # invoca o metodo de criacao e configuracao da tela de login
        self.rh_frame()         # invoca o metodo de criacao e configuracao do frame de tela
        self.rh_widgets()       # invoca o metodo de criacao e configuracao de widgets
        self.rhroot.mainloop()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def rh_screen(self):
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

        self.bt_remove = Button(self.frame1, text='Remove', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_remove) # setup 
        self.bt_remove.place(relx=0.01, rely=0.09, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_change = Button(self.frame1, text='Change', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_change) # setup 
        self.bt_change.place(relx=0.01, rely=0.17, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_search = Button(self.frame1, text='Search', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.frame_search) # setup 
        self.bt_search.place(relx=0.01, rely=0.25, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        self.bt_exitmenu = Button(self.frame1, text='Exit', bd=4, bg='grey', activebackground='white', activeforeground='black', font=('comic-sans', 8, 'bold', 'italic'), command=self.rhroot.destroy) # setup 
        self.bt_exitmenu.place(relx=0.01, rely=0.33, relwidth=1, relheight=0.07)                                                                                                                        # posicao

        #--------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def frame_insert(self): # método de criacao de frame

            self.frame2 = Frame(self.rhroot, bd = 4, bg='white', highlightbackground='black', highlightthickness=3) # setup 
            self.frame2.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                      # posicao

            # Widgets

            self.lb_name = Label(self.frame2, text = 'Name:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_name.place(relx=0.001, rely=0.01, relwidth=0.1, relheight=0.1)                                   # posicao

            self.lb_birth = Label(self.frame2, text = 'Birth:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_birth.place(relx=0.015, rely=0.07, relwidth=0.1, relheight=0.1)                                    # posicao

            self.lb_nif = Label(self.frame2, text = 'NIF:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_nif.place(relx=0.015, rely=0.013, relwidth=0.1, relheight=0.1)                                 # posicao

            self.lb_marital = Label(self.frame2, text = 'Marital Status:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_marital(relx=0.015, rely=0.019, relwidth=0.1, relheight=0.1)                                                  # posicao

            self.lb_nationality = Label(self.frame2, text = 'Nationality:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_nationality.place(relx=0.025, rely=0.07, relwidth=0.1, relheight=0.1)                                          # posicao

            self.lb_sex = Label(self.frame2, text = 'Sex:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_sex.place(relx=0.015, rely=0.031, relwidth=0.1, relheight=0.1)                                 # posicao

            self.lb_address = Label(self.frame2, text = 'Address:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_address.place(relx=0.015, rely=0.037, relwidth=0.1, relheight=0.1)                                     # posicao

            self.lb_phone = Label(self.frame2, text = 'Phone:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_phone.place(relx=0.015, rely=0.043, relwidth=0.1, relheight=0.1)                                   # posicao

            self.lb_email = Label(self.frame2, text = 'Email:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_email.place(relx=0.015, rely=0.049, relwidth=0.1, relheight=0.1)                                   # posicao

            self.lb_pos = Label(self.frame2, text = 'Employee Position:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_pos.place(relx=0.015, rely=0.055, relwidth=0.1, relheight=0.1)                                               # posicao

            self.lb_date_adm = Label(self.frame2, text = 'Admission Date:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_date_adm(relx=0.015, rely=0.061, relwidth=0.1, relheight=0.1)                                                  # posicao

            self.lb_salary = Label(self.frame2, text = 'Salary:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_salary.place(relx=0.015, rely=0.067, relwidth=0.1, relheight=0.1)                                    # posicao

            self.lb_turn = Label(self.frame2, text = 'Work Shift:', bg='white', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_turn.place(relx=0.015, rely=0.073, relwidth=0.1, relheight=0.1)                                        # posicao

            #--------------------------------------

    def frame_remove(self): # método de criacao de frame
         
            self.frame3 = Frame(self.rhroot, bd = 4, bg='yellow', highlightbackground='black', highlightthickness=3) # setup 
            self.frame3.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                       # posicao

            #--------------------------------------

    def frame_change(self): # método de criacao de frame
         
            self.frame4 = Frame(self.rhroot, bd = 4, bg='green', highlightbackground='black', highlightthickness=3) # setup 
            self.frame4.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                      # posicao

            #--------------------------------------

    def frame_search(self): # método de criacao de frame
         
            self.frame5 = Frame(self.rhroot, bd = 4, bg='blue', highlightbackground='black', highlightthickness=3) # setup 
            self.frame5.place(relx=0.2, rely=0.001, relwidth=0.8, relheight=1)                                     # posicao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def run(self): # metodo para rodar o loop do form

        self.rhroot.mainloop() # loop do form

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
RHScreen()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

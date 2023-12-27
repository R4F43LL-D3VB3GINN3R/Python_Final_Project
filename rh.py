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

            #--------------------------------------

            # Widgets - [Molduras]

            self.canvas_bt = Canvas(self.frame2, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
            self.canvas_bt.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.65)  # posiciona a moldura

            self.canvas_bt = Canvas(self.frame2, bd=4, bg='grey', highlightbackground='grey', highlightthickness=3, relief='sunken') # objeto recebe uma moldura
            self.canvas_bt.place(relx=0.01, rely=0.67, relwidth=0.98, relheight=0.32)  # posiciona a moldura        

            #--------------------------------------

            # Widgets - [Labels]

            self.lb_title1 = Label(self.frame2, text = 'Personal Info', bg='grey', font=('comic-sans', 15, 'bold', 'italic')) # setup
            self.lb_title1.place(relx=0.33, rely=0.03, relwidth=0.3, relheight=0.05)                                          # posicao

            self.lb_name = Label(self.frame2, text = 'Name:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_name.place(relx=0.14, rely=0.1, relwidth=0.09, relheight=0.05)                                  # posicao

            self.lb_id = Label(self.frame2, text = 'ID:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_id.place(relx=0.16, rely=0.16, relwidth=0.07, relheight=0.05)                               # posicao

            self.lb_code = Label(self.frame2, text = 'Code:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_code.place(relx=0.3, rely=0.16, relwidth=0.07, relheight=0.05)                                  # posicao

            self.lb_age = Label(self.frame2, text = 'Age:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_age.place(relx=0.46, rely=0.16, relwidth=0.07, relheight=0.05)                                  # posicao

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
            self.lb_title2.place(relx=0.33, rely=0.69, relwidth=0.3, relheight=0.05)                                      # posicao 

            self.lb_pos = Label(self.frame2, text = 'Job Position:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_pos.place(relx=0.065, rely=0.77, relwidth=0.16, relheight=0.05)                                          # posicao 

            self.lb_salary = Label(self.frame2, text = 'Salary:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_salary.place(relx=0.13, rely=0.83, relwidth=0.1, relheight=0.05)                                    # posicao    

            self.lb_turn = Label(self.frame2, text = 'Work Shift:', bg='grey', font=('comic-sans', 10, 'bold', 'italic')) # setup
            self.lb_turn.place(relx=0.085, rely=0.89, relwidth=0.14, relheight=0.05)                                        # posicao 

            #--------------------------------------

            # Widgets - [Entradas]

            self.in_name = Entry(self.frame2, bd=4)                               # setup
            self.in_name.place(relx=0.23, rely=0.1, relwidth=0.7, relheight=0.05) # posicao

            self.in_id = Entry(self.frame2, bd=4)                                 # setup
            self.in_id.place(relx=0.23, rely=0.16, relwidth=0.05, relheight=0.05) # posicao

            self.in_code = Entry(self.frame2, bd=4)                                 # setup
            self.in_code.place(relx=0.39, rely=0.16, relwidth=0.05, relheight=0.05) # posicao

            self.in_age = Entry(self.frame2, bd=4)                                 # setup
            self.in_age.place(relx=0.54, rely=0.16, relwidth=0.05, relheight=0.05) # posicao

            self.in_sex = Entry(self.frame2, bd=4)                                 # setup
            self.in_sex.place(relx=0.23, rely=0.22, relwidth=0.04, relheight=0.05) # posicao

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
            self.in_turn.place(relx=0.23, rely=0.89, relwidth=0.04, relheight=0.05) # posicao 

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

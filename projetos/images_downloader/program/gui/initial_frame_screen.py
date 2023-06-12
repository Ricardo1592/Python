import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk

class InitialFrameScreen(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self._set_appearance_mode("dark")
        self.main_screen = parent
        
        # TESTE DO TAMANHO DO FRAME 
        # label1 = ttk.Label(self, background='red')
        # label1.pack(expand=True, fill='both')
        
        # self._set_appearance_mode("dark")
        # self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_widgets()
        self.pack(expand=True, fill='both')

    def show_widgets(self):    

        # self._set_appearance_mode("dark")    
        button1 = ctk.CTkButton(self, text='FOLDER IMAGES', command=lambda: self.go_to_folder_images(self.main_screen.initial_frame, self.main_screen.folder_images_frame))
        button1.place(relx=0.1425, rely=0.475, relwidth=0.35, relheight=0.08)
        # button1.pack(side='left', expand=True, fill='x') 

        button2 = ctk.CTkButton(self, text='SCRAPPER IMAGES')
    
        button2.place(relx=0.55, rely=0.475, relwidth=0.35, relheight=0.08)
        # button2.pack(side='left', expand=True, fill='x') 

    def go_to_folder_images(self, initial_frame: ctk.CTkFrame, new_frame: ctk.CTkFrame):
        
        # Abordagem1 seria por destruição do frame e criação de um novo,
        # logo o objeto teria que ser criado novamente
        # para poder voltar a tela anterior --> https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter, https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter
        
        # initial_frame.destroy()
        # new_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # No caso desse programa, é desejável que as imagens já carregadas
        # anteriormente não sejam e destruídas e carregadas de novo,
        # por isso usarei a abordagem de 
        # pack forget --> https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter, https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter
        initial_frame.pack_forget()
        new_frame.pack(expand=True, fill='both')
        
       

        



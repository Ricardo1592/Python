import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk

class InitialFrameScreen(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # TESTE DO TAMANHO DO FRAME 
        # label1 = ttk.Label(self, background='red')
        # label1.pack(expand=True, fill='both')
        
        self._set_appearance_mode("dark")
        # self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.pack(expand=True, fill='both')
        self.show_widgets()


    def show_widgets(self):    

        self._set_appearance_mode("dark")    
        button1 = ctk.CTkButton(self, text='FOLDER IMAGES')
        button1.place(relx=0.1425, rely=0.475, relwidth=0.35, relheight=0.08)
        # button1.pack(side='left', expand=True, fill='x') 

        button2 = ctk.CTkButton(self, text='SCRAPPER IMAGES')
        button2.place(relx=0.55, rely=0.475, relwidth=0.35, relheight=0.08)
        # button2.pack(side='left', expand=True, fill='x') 
        



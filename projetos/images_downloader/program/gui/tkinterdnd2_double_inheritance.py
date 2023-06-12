from tkinter import StringVar, TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter as ctk


# double inheritance para pode arrastar(drag) um arquivo para
# o entry widget --> https://stackoverflow.com/questions/75526264/using-drag-and-drop-files-or-file-picker-with-customtkinter 
# https://stackoverflow.com/questions/14267900/drag-and-drop-explorer-files-to-tkinter-entry-widget
class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

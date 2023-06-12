import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from gui.tkinterdnd2_double_inheritance import Tk
from gui.initial_frame_screen import InitialFrameScreen
from gui.folder_images_screen import FolderImagesScreen

class MainScreen(Tk):

    def __init__(self, size: tuple = (2000, 1000)) -> None:
        # Inicializa uma instância de ctk.CTk, equivalente a --> root = ctk.CTk()
        super().__init__()
        
        # self._set_appearance_mode("dark")
        self.size = size
        self.title('Images Downloader')
        self.geometry(f'{self.size[0]}x{self.size[1]}+100+200')
        # self.resizable(False, False)

        self.initial_frame = InitialFrameScreen(self)
        self.folder_images_frame = FolderImagesScreen(self)
        # self.scrapper_images_frame = InitialFrameScreen(self)



        # Inicializa o loop do programa, equivalente a --> root.mainloop()
        self.mainloop()



if __name__ == '__main__':
    app = MainScreen()

    
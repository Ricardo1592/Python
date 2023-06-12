import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD

def handle_drop(event):
    folder = event.data
    entry_caminho.delete(0, tk.END)
    entry_caminho.insert(tk.END, folder)

# Cria a janela principal
janela = TkinterDnD.Tk()

# Cria o widget Entry
entry_caminho = tk.Entry(janela, width=50)

# Configura o suporte a arrastar e soltar no Entry
entry_caminho.drop_target_register(DND_FILES)
entry_caminho.dnd_bind('<<Drop>>', handle_drop)
entry_caminho.pack()

# Inicia o loop principal da janela
janela.mainloop()

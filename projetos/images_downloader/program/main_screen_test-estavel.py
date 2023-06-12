from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Button, Tk, Canvas, Scrollbar, Frame, VERTICAL, N, NW, Label, Checkbutton, IntVar
import customtkinter as ctk 

class ImagemItem:
    def __init__(self, image, checkbox, image_number: int, path: Path):
        self.image = image
        self.checkbox = checkbox
        self.image_number = image_number
        self.path = path

def exibir_imagens():
    # Pasta contendo as imagens
    pasta = Path.cwd()
    images_path = pasta / 'program' / 'utils' / 'pics'

    # Cria uma janela
    janela = ctk.CTk()
    janela.title("Exibição de Imagens")
    janela.geometry('2000x1000')
    janela.resizable(False, False)
    ctk.set_appearance_mode("dark")
    global shift_pressed

    frame_left = ctk.CTkFrame(janela, width=300, height=800)
    frame_left.pack(side='left', padx=30, pady=50)
    # Cria o canvas e o scrollbar vertical
    canvas = ctk.CTkCanvas(janela, width=2900, height=1500)
    canvas.pack(side='left', expand=True, fill='both')

    # Cria um frame dentro do canvas para conter as imagens
    frame_canvas = ctk.CTkFrame(canvas)
    canvas.create_window((0, -10), window=frame_canvas, anchor='nw')

    # Função para tratar o evento de pressionar a tecla Shift
    def shift_pressionado(event):
        global shift_pressed
        shift_pressed = True

    # Função para tratar o evento de soltar a tecla Shift
    def shift_soltado(event):
        global shift_pressed
        shift_pressed = False

    # Função para tratar o evento de clique em um checkbox
    def checkbox_clicado(index):
        global shift_pressed, ultimo_checkbox_clicado
        if shift_pressed and ultimo_checkbox_clicado is not None:
            inicio_sequencia = min(ultimo_checkbox_clicado, index)
            fim_sequencia = max(ultimo_checkbox_clicado, index)
            for i in range(inicio_sequencia + 1, fim_sequencia):
                item = itens_imagem[i]
                item.checkbox.var.set(True)
        ultimo_checkbox_clicado = index

    # Função para imprimir os checkboxes clicados
    def imprimir_checkboxes_clicados():
        checkboxes_clicados = [item.checkbox.var.get() for item in itens_imagem]
        imagens_selecionadas = [item.image for item in itens_imagem if item.checkbox.var.get()]
        image_number = [item.image_number for item in itens_imagem if item.checkbox.var.get()]
        image_path = [item.path for item in itens_imagem if item.checkbox.var.get()]
        print("Checkboxes clicados:", checkboxes_clicados)
        print("Image number: ", image_number)
        print("Image path: ", image_path)

    # Configuração do layout em grid
    num_colunas = 5  # Número de imagens por linha
    coluna_atual = 0
    linha_atual = 0
    image_number = 1
    # Obter a lista de arquivos na pasta
    arquivos = list(images_path.glob('*'))

    # Lista para armazenar os itens de imagem
    itens_imagem = []

    # Exibir as imagens no canvas
    for i, arquivo in enumerate(arquivos):
        # Carrega a imagem
        image = Image.open(arquivo)
        image.thumbnail((230, 230))
        image_size = image.size
        # width, height = image_size
        # width = width/8 if width < 2500 else width/20
        # height = height/8 if width < 2500 else height/20
        # image_size = (width, height)
        # print('image size -- ', image_size)
        # Redimensiona a imagem para um tamanho fixo (thumbnail)
        

        # Cria um PhotoImage do tkinter
        imagem = ImageTk.PhotoImage(image)
        imagemCTk = ctk.CTkImage(image, size=image_size)

        # Cria um Checkbutton para cada imagem
        var = IntVar()
        checkbox = ctk.CTkCheckBox(frame_canvas, variable=var, command=lambda i=i: checkbox_clicado(i), text='')
        checkbox.var = var

        # Cria um Label para exibir a imagem
        label = ctk.CTkLabel(frame_canvas, image=imagemCTk, text='')
        label.image = imagemCTk

        # Posiciona o Checkbutton e o Label no grid
        label.grid(row=linha_atual, column=coluna_atual, padx=1, pady=5)
        checkbox.grid(row=linha_atual, column=coluna_atual + 1, padx=1, pady=5)
        if image_number == 1:
            label.grid(row=linha_atual, column=coluna_atual, padx=1, pady=25)
            checkbox.grid(row=linha_atual, column=coluna_atual + 1, padx=1, pady=25)


        # Cria um item de imagem com o Label e o Checkbutton correspondentes
        item_imagem = ImagemItem(image, checkbox, image_number, arquivo)
        itens_imagem.append(item_imagem)

        # Atualiza a coluna e a linha atual
        coluna_atual += 2
        if coluna_atual >= num_colunas * 2:
            coluna_atual = 0
            linha_atual += 1
        image_number += 1

    # Variável para armazenar o último checkbox clicado
    ultimo_checkbox_clicado = None

    # Configura os manipuladores de eventos do teclado
    janela.bind("<Shift_L>", shift_pressionado)
    janela.bind("<KeyRelease-Shift_L>", shift_soltado)

    # Cria o scrollbar vertical vinculado ao canvas
    scrollbar = ctk.CTkScrollbar(janela, command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    # Configura o canvas para controlar a rolagem do frame_canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Função para rolar o canvas com o mousewheel
    def rolar_mousewheel(event):
        canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    # Vincula o evento do mousewheel à função de rolagem
    canvas.bind_all("<MouseWheel>", rolar_mousewheel)

    # Ajusta a posição do scrollbar vertical
    canvas.yview_moveto(0)

    # Botão de teste para imprimir os checkboxes clicados
    botao_teste = ctk.CTkButton(frame_canvas, text="Imprimir Checkboxes Clicados", command=imprimir_checkboxes_clicados, width=400)
    botao_teste.grid(row=linha_atual + 1, column=0, columnspan=num_colunas * 2, padx=2, pady=20)

    # Inicia o loop principal da janela
    janela.mainloop()


# Chama a função para exibir as imagens
shift_pressed = False
exibir_imagens()

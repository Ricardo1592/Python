import tkinter as tk
from tkinter import StringVar, TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk
from gui.tkinterdnd2_double_inheritance import Tk
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Button, Tk, Canvas, Scrollbar, Frame, VERTICAL, N, NW, Label, Checkbutton, IntVar
# Para mudar a velocidade do scroll ir na classe --> ctk.CTkScrollableFrame
# e mudar em --> def _mouse_wheel_all e mudar a divisão: -int(event.delta / 6) para: -int(event.delta / 3)
class FolderImagesScreen(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        # self._set_appearance_mode("dark")
        
        # Para testar o tamanho do frame

        # label1 = ctk.CTkLabel(self, bg_color='blue')
        # label1.pack(expand=True, fill='both')
        self.master = parent
        frame_left_side = FrameLeftSideScrollable(self)
        frame_left_side.place(relx=0.220, rely=0.01, relwidth=1, relheight=0.98)

        frame_right_side = FrameRightSide(self, frame_left_side)
        frame_right_side.place(relx=0.012, rely=0.1, relwidth=0.2, relheight=0.8)
        self.folder_path :Path = None
        

        # O frame dessa tela, ocupa tudo, e só
        # será revelado quando for chamado por algum botão

        # self.place(relx=0, rely=0, relwidth=1, relheight=1)


class FrameRightSide(ctk.CTkFrame):

    def __init__(self, parent, frame_left_side):
        super().__init__(parent)  
        # self._set_appearance_mode("dark") 
        self.folder_path: Path = None
        self.parent = parent
        self.frame_left_side = frame_left_side
        self.folders = ''
        
        # Teste para saber do tamanho do frame
        # label_right_side = ctk.CTkLabel(self, bg_color='red')
        # label_right_side.pack(expand=True, fill='both')

        # Para poder arrastar uma pasta para o entry box --> https://stackoverflow.com/questions/75526264/using-drag-and-drop-files-or-file-picker-with-customtkinter
        # instalação: pip install tkinterdnd2 
        # https://stackoverflow.com/questions/14267900/drag-and-drop-explorer-files-to-tkinter-entry-widget
        
        self.folder_path_Svar = tk.StringVar()
        self.folder_path_Svar.set(25*' '+'DROP AN IMAGE FOLDER HERE')
        
        self.entryWidget = ctk.CTkEntry(self, textvariable=self.folder_path_Svar)

        self.button_show_images = ctk.CTkButton(self, text="Show Images", command=self.show_images)
        self.button_reset_paths = ctk.CTkButton(self, text="Reset Paths", command=self.clear_paths)
        self.button_clear_selection = ctk.CTkButton(self, text="Clear Selection", command=self.clear_selection)

        self.entryWidget.drop_target_register(DND_ALL)
        self.entryWidget.dnd_bind("<<Drop>>", self.get_path)

        # entryWidget.pack(side='top', padx=5, pady=5)
        self.entryWidget.place(relx=0.025, rely=0.1, relwidth=0.95, relheight=0.25)
        self.button_show_images.place(relx=0.025, rely=0.375, relwidth=0.95, relheight=0.1)
        self.button_reset_paths.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.025)

        # Segunda entrybox
        self.tags_var = tk.StringVar()
        self.tags_var.set('')
        
        self.tags = ctk.CTkEntry(self, textvariable=self.tags_var)

        self.button_add_tags = ctk.CTkButton(self, text="Add Tags", command=self.add_tags)

        self.tags.place(relx=0.025, rely=0.55, relwidth=0.95, relheight=0.1)
        self.button_add_tags.place(relx=0.025, rely=0.67, relwidth=0.4625, relheight=0.05)
        self.button_clear_selection.place(relx=0.5125, rely=0.67, relwidth=0.4625, relheight=0.05)

    def get_path(self, event):
        if 'DROP AN IMAGE FOLDER HERE' in self.folder_path_Svar.get():
            self.folder_path_Svar.set('')
        folder_list = ['']
        self.frame_left_side.folder_paths = []
        print("Entry box field: ", event.data)
        # print(type(event.data))
        folder_path = event.data
        if not event.data.endswith('}'): 
            folder_path = '{' + event.data + '}'
        if self.folder_path_Svar.get():
            previous_path = self.folder_path_Svar.get()  
        else:
            self.folder_path_Svar.set(folder_path)
            previous_path = ''
        if previous_path:
            if folder_path not in previous_path:
                folder_path = self.folder_path_Svar.get() + " " + folder_path 
            else:
                folder_path.replace(previous_path, '')  
                folder_path = self.folder_path_Svar.get() + " " + folder_path
           
        print("folder path -- ", folder_path) 
        current_path = folder_path         
        if folder_path.endswith('}'):
            folder_list = folder_path.split('}')
            folder_list = folder_list[:-1]
            if not folder_path.startswith(' '):
                folder_list[0] = ' ' + folder_list[0]
            print(folder_list) 
        else:
            folder_list[0] = folder_path   
            folder_list[0] = ' ' + folder_list[0] 

        print('folder list: ', folder_list)    
        for folder in folder_list:
            # remove o espaço vazio no início
            folder_path = folder[1:]
            current_path = folder[1:]
            folder_path = folder_path.replace('{', '')
            folder_path = folder_path.replace('}', '')
            print("remove { --> ", folder_path)
            print('image path --> ', folder_path)
            folder_path = Path(folder_path)
            print('image Path --> ', folder_path)
            print('Is file:', folder_path.is_dir())
            print('Is file:', folder_path.exists())
            if folder_path.is_dir() and folder_path.exists():
                self.folder_path = folder_path
                self.frame_left_side.folder_path = folder_path
                self.frame_left_side.folder_paths.append(folder_path)
                
            # print('folder path is --> ', str(self.frame_left_side.folder_path ))   
            current_path = current_path + '}'
            if folder_path.is_dir() and current_path not in self.folders:
                self.folders = self.folders + current_path
                self.folder_path_Svar.set(self.folders)
            if not self.folder_path.is_dir():
                self.folder_path_Svar.set(f'Not a folder!\nCurrent folder is:\n{str(self.folder_path)}')   

    def show_images(self):
        
        if self.folder_path and self.folder_path_Svar.get():
            # print('will show images')
            # self.frame_left_side.destroy()
            self.frame_left_side = FrameLeftSideScrollable(self.frame_left_side.parent, self.folder_path, self.frame_left_side.folder_paths)
            self.frame_left_side.place(relx=0.237, rely=0.01, relwidth=0.763, relheight=0.98)
            self.frame_left_side.show_images()
        if not self.folder_path_Svar.get():
            print('destroying frame...')
            self.frame_left_side.destroy()
            self.frame_left_side = FrameLeftSideScrollable(self.parent)
            self.frame_left_side.place(relx=0.237, rely=0.01, relwidth=0.763, relheight=0.98)
            
    def add_tags(self):
        if self.frame_left_side.images_loaded:
            # print('Addingg tags --> ', self.tags_var.get())
            self.frame_left_side.tags = self.tags_var.get() 
            self.frame_left_side.add_tags_to_image() 

    def clear_selection(self):
        # print(self.frame_left_side.checkboxs_selected)
        for checkbox in self.frame_left_side.checkboxs_selected:
            checkbox.var.set(False)

    def clear_paths(self):
        # print(self.frame_left_side.checkboxs_selected)
        self.folder_path_Svar.set('')
         
class FrameLeftSideScrollable(ctk.CTkScrollableFrame):
    
    def __init__(self, parent, folder_path: Path = None, folder_paths: list = [], tags: str = None):
        super().__init__(parent)
        self.folder_path = folder_path
        self.folder_paths = folder_paths
        self.parent = parent
        # Configuração do layout em grid
        self.num_colunas = 5  # Número de imagens por linha
        self.coluna_atual = 0
        self.linha_atual = 0
        self.image_number = 1
        self.shift_pressed = False 
        self.ultimo_checkbox_clicado = None
        self.images_loaded = False
        self.tags = tags
        self.checkboxs_selected = []

        # Lista para armazenar os itens de imagem
        self.itens_imagem = []
        self.parent.master.bind("<Shift_L>", self.shift_pressionado)
        self.parent.master.bind("<KeyRelease-Shift_L>", self.shift_soltado) 

    def show_images(self):
        # print("folder path--> ", self.folder_path)
        arquivos = []
        for folder in self.folder_paths:
            files = list(folder.glob('*.jpg*'))
            print("files -- ", files)
            arquivos.extend(files)
        # print(arquivos)
        for i, arquivo in enumerate(arquivos):
            # Carrega a imagem
            image = Image.open(arquivo)
            image.thumbnail((265, 265))
            image_size = image.size
            # print('image size ', image_size)
        
            # Cria um PhotoImage do tkinter
            imagemCTk = ctk.CTkImage(image, size=image_size)

            # Cria um Checkbutton para cada imagem
            
            var = IntVar()
            checkbox = ctk.CTkCheckBox(self, variable=var, text='', command=lambda i=i: self.checkbox_clicado(i), width=0.2)
            # print("checkbox width ", checkbox.winfo_width())
            checkbox.var = var

            # Cria um Label para exibir a imagem
            label = ctk.CTkLabel(self, image=imagemCTk, text='')
            label.image = imagemCTk
            # print("label width ", label.winfo_width())

            # Posiciona o Checkbutton e o Label no grid
            label.grid(row=self.linha_atual, column=self.coluna_atual, padx=1, pady=5, sticky='ns')
            checkbox.grid(row=self.linha_atual, column=self.coluna_atual+1, padx=1, pady=5, sticky='w')
            # if image_number == 1:
            #     label.grid(row=self.linha_atual, column=self.coluna_atual, padx=1, pady=25)
            #     # checkbox.grid(row=self.linha_atual, column=self.coluna_atual + 1, padx=1, pady=25)


            # Cria um item de imagem com o Label e o Checkbutton correspondentes
            item_imagem = ImagemItem(image, checkbox, self.image_number, arquivo)
            self.itens_imagem.append(item_imagem)

            # Atualiza a coluna e a linha atual
            self.coluna_atual += 2
            if self.coluna_atual >= self.num_colunas * 2:
                self.coluna_atual = 0
                self.linha_atual += 1
            self.image_number += 1   
            self.images_loaded = True

    def checkbox_clicado(self, index):
        print("checkbox clicado: ", index)
        if self.shift_pressed and self.ultimo_checkbox_clicado is not None:
            inicio_sequencia = min(self.ultimo_checkbox_clicado, index)
            fim_sequencia = max(self.ultimo_checkbox_clicado, index)
            for i in range(inicio_sequencia + 1, fim_sequencia):
                item = self.itens_imagem[i]
                item.checkbox.var.set(True)
                self.checkboxs_selected.append(item.checkbox)
        self.ultimo_checkbox_clicado = index
        self.checkboxs_selected.append(self.itens_imagem[index].checkbox)

    def shift_pressionado(self, event):
        # print('shift pressed')
        self.shift_pressed = True

    # Função para tratar o evento de soltar a tecla Shift
    def shift_soltado(self, event):
        # print('shift soltado')
        self.shift_pressed = False

    def add_tags_to_image(self):
        checkboxes_clicados = []
        imagens_selecionadas = []
        image_numbers = []
        images_path = []
        for item in self.itens_imagem:
            if item.checkbox.var.get():
                checkboxes_clicados.append(item.checkbox.var.get())
                imagens_selecionadas.append(item.image)
                image_numbers.append(item.image_number)
                images_path.append(item.path)
                if self.tags not in item.path.stem: 
                    new_name = self.tags + " " + item.path.stem
                    item.path.rename(item.path.with_stem(new_name))
                
        print("Checkboxes clicados:", checkboxes_clicados)
        print("Image number: ", image_numbers)
        print("Image path: ", images_path)

                




class ImagemItem:
    def __init__(self, image, checkbox, image_number: int, path: Path):
        self.image = image
        self.checkbox = checkbox
        self.image_number = image_number
        self.path = path












class FrameLeftSide(ctk.CTkFrame):
    
    def __init__(self, parent, folder_path: Path = None):
        super().__init__(parent)
        self._set_appearance_mode('dark')
        self.folder_path = folder_path


        
        # Jeito antigo: Utilizando o canvas para o scroll
        # canvas = ctk.CTkCanvas(self, bg='red', scrollregion=(0, 0, 3000, 10000)) 
        # canvas.create_line(0, 0, 3000, 10000, fill='green', width=10)
        # canvas.pack(expand=True, fill='both')

        # scrollbar_vertical = ctk.CTkScrollbar(self, orientation='vertical', command=canvas.yview)
        # scrollbar_vertical.place(relx=1, rely=0, relheight=1, anchor='ne') 
        # canvas.configure(yscrollcommand=scrollbar_vertical.set)

        # self._set_appearance_mode("dark") 
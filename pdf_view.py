# pdf_view.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk  # Importe ttk para a barra de progresso
from pdf_model import PDFProcessor

class PDFGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Filtrar Palavra em PDF")

        # Adicione um ícone à janela
        self.iconbitmap("icone.ico")  # Substitua "icone.ico" pelo caminho do seu ícone

        # Adicione um menu
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        arquivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
        arquivo_menu.add_command(label="Sair", command=self.sair)

        # Elementos da interface gráfica
        tk.Label(self, text="Palavra a Filtrar:").pack(pady=10)
        self.palavra_entry = tk.Entry(self)
        self.palavra_entry.pack(pady=10)

        self.selecionar_arquivo_btn = tk.Button(self, text="Selecionar Arquivo PDF", command=self.processar_arquivo)
        self.selecionar_arquivo_btn.pack(pady=20)

        self.resultado_text = tk.Text(self, height=10, width=50)
        self.resultado_text.pack()

        # Adicione uma barra de progresso (ttk.Progressbar)
        self.barra_progresso = ttk.Progressbar(self, mode="indeterminate")
        self.barra_progresso.pack(pady=10)

    def sair(self):
        self.destroy()

    def processar_arquivo(self):
        try:
            pdf_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])

            if not pdf_path:
                messagebox.showinfo("Aviso", "Nenhum arquivo PDF selecionado.")
                return

            palavra_a_filtrar = self.palavra_entry.get()

            if not palavra_a_filtrar:
                messagebox.showinfo("Aviso", "Por favor, insira uma palavra para filtrar.")
                return

            self.barra_progresso.start()  # Inicia a barra de progresso

            # Simula algum processamento demorado (como o carregamento de um arquivo grande)
            self.after(2000, lambda: self.realizar_processamento(pdf_path, palavra_a_filtrar))
        except FileNotFoundError:
            self.barra_progresso.stop()  # Para a barra de progresso em caso de erro
            messagebox.showerror("Erro", "Arquivo não encontrado. Por favor, escolha um arquivo válido.")
        except Exception as e:
            self.barra_progresso.stop()  # Para a barra de progresso em caso de erro
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {str(e)}")

    def realizar_processamento(self, pdf_path, palavra_a_filtrar):
        pdf_processor = PDFProcessor()
        resultados = pdf_processor.filtrar_palavra(pdf_path, palavra_a_filtrar)

        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, f'Palavra "{palavra_a_filtrar}" encontrada nas seguintes instâncias: {resultados}')

        self.barra_progresso.stop()  # Para a barra de progresso após o processamento

if __name__ == "__main__":
    app = PDFGUI()
    app.mainloop()

import re
from PyPDF2 import PdfReader
from tkinter import Tk, filedialog


def selecionar_arquivo():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return file_path

def contar_paginas(reader):
    return len(reader.pages)


def extrair_texto(reader):
    textos = [page.extract_text() for page in reader.pages]
    return textos


def buscar_palavra_chave(textos, palavra):
    for i, text in enumerate(textos):
        if palavra in text:
            print(f"🔍 Palavra-chave '{palavra}' encontrada na página {i + 1}:")
            for line in text.split("\n"):
                if palavra in line:
                    print(line)


def buscar_padroes(textos):
    for i, text in enumerate(textos):
        cpfs = re.findall(r"\d{3}\.\d{3}\.\d{3}-\d{2}", text)
        datas = re.findall(r"\d{2}/\d{2}/\d{4}", text)
        processos = re.findall(r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}", text)

        if cpfs or datas or processos:
            print(f"\n📄 Página {i + 1}:")
            if cpfs:
                print("🔢 CPFs encontrados:", cpfs)
            if datas:
                print("📅 Datas encontradas:", datas)
            if processos:
                print("⚖️ Processos encontrados:", processos)


def ler_pdf():
    file_path = selecionar_arquivo()

    if file_path:
        with open(file_path, "rb") as file:
            reader = PdfReader(file)


            num_paginas = contar_paginas(reader)
            print(f"\n📑 O PDF possui {num_paginas} páginas.\n")

            textos = extrair_texto(reader)

            buscar_palavra_chave(textos, "Advogados")

            buscar_padroes(textos)

    else:
        print("❌ Nenhum arquivo selecionado.")


ler_pdf()


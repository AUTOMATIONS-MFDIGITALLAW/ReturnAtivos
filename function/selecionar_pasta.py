import os
from tkinter import filedialog
from function.logger import log

def selecionar_pasta_pdfs():
    """
    Abre um seletor de diretórios para escolher a pasta que contém os PDFs.

    :return: Caminho da pasta selecionada (str) ou None se o usuário cancelar.
    """
    pasta_selecionada = filedialog.askdirectory(title="Selecione a pasta dos PDFs")

    if pasta_selecionada:
        log.success(f"Pasta de PDFs selecionada: {pasta_selecionada}")
        return pasta_selecionada
    else:
        log.warning("Nenhuma pasta selecionada")
        return None

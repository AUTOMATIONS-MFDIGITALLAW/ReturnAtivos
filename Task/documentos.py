from time import sleep

from function.imports import (
    time,
    pya,
    pyperclip,
    pyautogui,
    searchimage,
    date_dois_dias,
    datetime,
    copiar
)
import os
import glob
from function.logger import log

def documentos(row, pasta_pdfs: str):
    """
    Usa a pasta de PDFs selecionada e insere o caminho do primeiro PDF encontrado.

    :param pasta_pdfs: Caminho da pasta onde os PDFs estão armazenados
    """
    if not pasta_pdfs or not os.path.exists(pasta_pdfs):
        log.error("Nenhuma pasta válida foi fornecida à função documentos().")
        return

    # Listar todos os arquivos PDF na pasta
    pdf_files = glob.glob(os.path.join(pasta_pdfs, "*.pdf"))

    if not pdf_files:
        log.warning("Nenhum arquivo PDF encontrado na pasta selecionada.")
        return

    # Seleciona o primeiro PDF encontrado
    pdf_path = pdf_files[0]
    log.info(f"Usando o arquivo PDF: {pdf_path}")

    # Automação interagindo com o sistema
    searchimage('documentos', 'documentos encontrado', 'documentos não encontrado')
    sleep(1)
    searchimage('adicionar', 'adicionar encontrado', 'adicionar não encontrado')
    sleep(1)
    searchimage('Selecionar_arquivo','Selecionar_arquivo encontrado', 'Selecionar_arquivo não encontrado')
    searchimage('Dialog','Dialog encontrado', 'Dialog não encontrado')
    for _ in range(5):
        pya.press('tab')
        sleep(0.1)
    pya.press('enter')
    pya.write(pdf_path)
    pya.press('enter')
    sleep(5)
    for _ in range(6):
        pya.press('tab')
        sleep(0.3)
    sleep(1)
    log.info('Colocando nome')
    pya.write(row(['PROCESSO]']))
    sleep(1)
    searchimage('Abrir','Abrir encontrado', 'Abrir não encontrado')
    log.success(f"Caminho do PDF digitado com sucesso: {pdf_path}")

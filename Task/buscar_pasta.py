from function.imports import (
    pya,
    pyperclip,
    time,
    click_and_fill,
    searchimage,
    copiar,
    pyautogui,
    FornecedorSelector,
)
from function.logger import log

def buscar_pasta():
    time.sleep(10)
    click_and_fill('processo', 'Processo encontrado!', 'processo não encontrado')
    time.sleep(4)
    #searchimage('abripasta', 'abripasta encontrado', 'abripasta não encontrado')
    #pya.write('85927')
    #searchimage('okamarelo', 'okamarelo encontrado', 'ok amarelo não encontrado')
    searchimage('incluir_processo', 'incluir Encontrado!', 'Incluir processo não encontrado!')
    time.sleep(5)
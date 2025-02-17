from function.imports import (
    pya,
    pyperclip,
    time,
    click_and_fill,
    searchimage,
    copiar,
    copiar2,
    pyautogui,
    FornecedorSelector,
)
from function.logger import log

def dados_gerais(row):
    print(f"Iniciando operação para o autor: {row['Autor']}")
    log.info(row['Autor'])
    log.info(row['Data de Captura'])
    test = copiar2(row["Data de Captura"])
    print(test)
    time.sleep(8)
    copiar(row["Data de Abertura"], date=True)
    click_and_fill('data da citacao', 'data citação encontrada', 'data citação não encontrada')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    click_and_fill('data da citacao2', 'data citação 2 encontrada', 'data citação 2 não encontrada')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('natureza', 'natureza Encontrado!', 'Campo natureza não encontrado!')
    texto = "AÇÕES PARA ACOMPANHAMENTO"
    pyperclip.copy(texto)
    time.sleep(2)
    log.info('texto copiado: ' + texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('TipoAcao', 'tipo de ação Encontrado!', 'tipo de ação não encontrado!')
    time.sleep(2)
    texto = "Indenizatória"
    pyperclip.copy(texto)
    log.info('texto copiado: ' + texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('procedimento', 'procedimento Encontrado!', ' procedimento não encontrado!')
    time.sleep(2)
    pya.press("backspace", presses=9)
    time.sleep(3)
    pya.write('Especial')
    time.sleep(3)
    nome_fornecedor = copiar(row["Fornecedor"].upper())
    nome_fornecedor = nome_fornecedor.upper()
    print(nome_fornecedor.upper())
    selector = FornecedorSelector(nome_fornecedor.upper()).get_fornecedor()
    print("Esse é o selector: ", selector)
    searchimage('unidadeOrganizacional', 'organizacional Encontrado!', ' organizacional não encontrado!')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(6)
    searchimage('unidadeCentral', 'Central Encontrado!', ' Central não encontrado!')
    time.sleep(3)
    pya.write('EMPRESAS TRIBANCO')
    time.sleep(8)
    pyautogui.scroll(-100)
    searchimage('Nota', 'Nota Encontrado!', ' nota não encontrado!')
    copiar(row["Relatos"])
    pyautogui.hotkey('ctrl', 'v')
    click_and_fill('subir', 'caminho para subir encontrado', 'caminho para subir nao encontrado')
    pyautogui.scroll(200)

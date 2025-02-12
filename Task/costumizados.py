from function.imports import (
    pyperclip,
    pya,
    time,
    endpoints,
    click_and_fill,
    searchimage,
    copiar,
    copiar2,
    pyautogui,
)

url = endpoints['TRI']

def costumizados(row):
    searchimage('costumizados','costumizados encontrado', 'costumizados não encontrado')
    searchimage('datadecaptura','datadecaptura encontrado','datadecaptura não escontrado')
    copiar(row["Data de Abertura"])
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    searchimage('cedido','cedido encontrado', 'cedido não encontrado')
    texto = 'NÃO CEDIDO'
    time.sleep(3)
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.scroll(-800)
    time.sleep(3)
    searchimage('classpos','classpos encontrado','classpos não encontrado')
    texto = 'Em Verificação'
    time.sleep(3)
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(6)
    click_and_fill('vazio','caminho vazio encontrado', 'Caminho vazio não encontrado')
    time.sleep(6)
    searchimage('salvar', 'salvar Encontrado', 'salvar não encontrado')
    time.sleep(15)

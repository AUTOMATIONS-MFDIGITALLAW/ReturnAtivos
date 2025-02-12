from function.imports import (
    time,
    pyperclip,
    pyautogui,
    searchimage
)

def object():
    searchimage('objetos', 'objeto encontrado', 'objetos não encontrado')
    time.sleep(1)
    searchimage('adicionar','adiconar encontrado', 'adicionar não encontrado')
    time.sleep(2)
    searchimage('objetoselecionar', 'objetoselecionar encontrado', 'objetoselecionar não encontrado')
    time.sleep(2)
    texto = "Reclamação Procon"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    searchimage('metodoatt', 'metodoatt encontrado','metodoatt nao encontrado')
    texto = "Não Se Aplica"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('infofinance','infofinance encontrado', 'infofinance não encontrado')
    time.sleep(1)
    searchimage('neutro', 'neutro encontrado','neutro não encontrado')
    time.sleep(1)
    searchimage('salvar', 'salvar Encontrado', 'salvar não encontrado')


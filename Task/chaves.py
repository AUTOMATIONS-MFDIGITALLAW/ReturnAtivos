from function.imports import (
    pyperclip,
    pya,
    time,
    endpoints,
    click_and_fill,
    searchimage,
    copiar,
    pyautogui,
)

url = endpoints['TRI']

def chaves():
    time.sleep(3)
    searchimage('palavraschaves', 'palavraschaves encontrado', 'palavraschaves não encontrado')
    time.sleep(3)
    searchimage('adicionar', 'adiconar encontrado', 'adicionar não encontrado')
    time.sleep(5)
    click_and_fill('procon','caminho procon encontrado', 'Caminho procon não encontrado')
    pya.write('PROCON')
    time.sleep(5)
    click_and_fill('procon2','caminho procon2 encontrado', 'Caminho procon2 não encontrado')
    searchimage('seta3', 'seta3 ancontrada', 'seta3 não encontrada')
    time.sleep(2)
    searchimage('salvar','salvar encontrado', 'salvar não encontrado')




from function.imports import (
    pya,
    time,
    endpoints,
    click_and_fill,
    searchimage,
    pyautogui,
)

url = endpoints['TRI']

def advogados():
    searchimage('advogados', 'advogados encontrado!', 'advogados não encontrado!')
    time.sleep(2)
    click_and_fill('buscaadv','caminho buscaaadv encontrado', 'Caminho buscaaadv não encontrado')
    pya.write('SEM ADV')
    time.sleep(2)
    searchimage('semadv', 'sem encontrado!', 'semadv não encontrado!')
    time.sleep(1)
    searchimage('setadireita', 'setadireita ancontrada', 'seta não encontrada')
    time.sleep(2)
    click_and_fill('vazio2','caminho vazio2 encontrado', 'Caminho vazio2 não encontrado')
    pyautogui.scroll(-500)
    time.sleep(5)
    click_and_fill('buscaempresa','caminho buscaempresa encontrado', 'Caminho buscaempresa não encontrado')
    time.sleep(2)
    pya.write('MEIRELES E FREITAS ADVOGADOS ASSOCIADOS - TRIBANCO')
    time.sleep(2)
    searchimage('meirelestribanco', 'meirelestribanco encontrando', 'meirelestribanco não encontrado')
    time.sleep(2)
    searchimage('setadireita', 'setadireita ancontrada', 'seta não encontrada')
    time.sleep(2)
    pyautogui.scroll(500)







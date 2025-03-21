from function.imports import (
    pya,
    pyperclip,
    time,
    endpoints,
    click_and_fill,
    searchimage,
    copiar,
    pyautogui,
    extrair_comarca,
)

url = endpoints['TRI']

def desdobramento(row):
    searchimage('desdobramento','desdobramento Encontrado!', 'desdobramento não encontrado')
    searchimage('dataeventos','dataeventos encontrado','dataeventos nao encontrado')
    copiar(row['Data de Abertura'], date=True)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('CNJ', 'CNJ Encontrado!', 'CNJ não encontrado!')
    searchimage('numerodoprocesso','numerodoprocesso Encontrado!', 'numerodoprocesso não encontrado')
    copiar(row["Número do Processo"])
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('tipodedesdobramento', 'tipodedesdobramento encontrado','tipodedesdobramento não encontrado')
    texto = "Ação de Indenização"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    click_and_fill('vazio2', 'caminho vazio2 encontrado!', "caminho vazio2 não enconrado")
    searchimage('Tribunal', 'tribunal encontrado!', 'tribunal não encontrado')
    time.sleep(1)
    pya.write('TJ')
    text = copiar(row["Foro"]).split("-")[1].strip()
    pyperclip.copy(text)
    time.sleep(3)
    #searchimage('administrativo', 'administrativo Encontrado!', ' administrativo não encontrado!') provavelmnete deletar
    searchimage('juris', 'juris encontrado!', 'juris não encontrado')
    time.sleep(1)
    pya.write('Proconsumidor') #Verificar como funcionar #Pegar planilha!
    time.sleep(3)
    searchimage('UF','UF encontrado!', 'UF não encontrado!')
    time.sleep(3)
    text = copiar(row["Foro"]).split("-")[1].strip()
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    click_and_fill('vazio', 'caminho vazio encontrado', 'Caminho vazio não encontrado')
    searchimage('comarca','comarca encontrada!','comarca não encontrada')
    pyperclip.copy(extrair_comarca(copiar(row["Foro"])))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    click_and_fill('vazio','caminho vazio encontrado', 'Caminho vazio não encontrado')






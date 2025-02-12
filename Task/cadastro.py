from function.imports import (
    pya,
    pyperclip,
    time,
    endpoints,
    searchimage,
    copiar,
    pyautogui
)


url = endpoints['TRI']

def cadastro(row):
    searchimage('cadastrorapido','cadastrorapido Encontrado!', 'cadastro não encontrado')
    searchimage('Entidade', 'entidade Encontrado!', 'entidade não encontrado!')
    pya.write(row['Autor'].upper())
    searchimage('tipodepessoa', 'tipodepessoa Encontrado!', 'tipodepessoa não encontrado!')
    texto = "Física"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('tipodedocumento','tipodedocumento Encontrado!', 'tipodedocumento não encontrado')
    pya.write('CPF')
    time.sleep(3)
    searchimage('numerododocumento','numerododocumento Encontrado!', 'numerododocumento não encontrado')
    copiar(row["Cpf/Cnpj"])
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
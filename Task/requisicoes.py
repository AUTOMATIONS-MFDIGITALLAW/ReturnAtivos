from pyautogui import click

from function.imports import (
    time,
    pya,
    pyperclip,
    pyautogui,
    searchimage,
    date_dois_dias,
    datetime,
    copiar,
    click_and_fill
)

def requisicoes(autor):
    searchimage('requisicoes','requisicoes encontrado','requisicoes não encontrado')
    searchimage('adicionar', 'adicionar encontrado', 'adicionar não encontrado')
    searchimage('titulo', 'titulo encontrado', 'titulo não encontrado')
    time.sleep(2)
    autor = autor
    pya.write(autor.upper() + ' ')
    time.sleep(2)
    copiar("Cpf/Cnpj")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('tipoderequisicao','tipoderequisicao encontrado','tipoderequisicao não encontrado')
    text = 'ANÁLISE / SUBSÍDIO DE PROCESSOS - PROCON'
    pyperclip.copy(text)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('responsavelexecutado','responsavelexecutado encontrado','responsavelexecutado não encontrado')
    text = 'MEIRELES (Thayssa Silva)'
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('detalhesrequisicao','detalhesrequisicao encontrado','detalhesrequisicao não encontrado')
    copiar("Relatos")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.scroll(-200)
    time.sleep(3)
    searchimage('unidadeorga','unidadeorga encontrado','unidadeorga não encontrado')
    pya.write('EMPRESAS TRIBANCO')
    time.sleep(4)
    pyautogui.scroll(-300)
    time.sleep(2)
    click_and_fill('requisicao','caminho requisição encontrado', 'Caminho requisição não encontrado')
    pya.write('MEIRELES (')
    time.sleep(4)
    searchimage('setadupla','setadupla encontrado','setadupla não encontrado')
    time.sleep(3)
    click_and_fill('requisicao','caminho requisição encontrado', 'Caminho requisição não encontrado')
    pya.write('MF DIGITAL')
    time.sleep(3)
    searchimage('setadupla','setadupla encontrado','setadupla não encontrado')
    time.sleep(2)
    searchimage('salvar','salvar encontrado', 'salvar não encontrado')
    print(autor)


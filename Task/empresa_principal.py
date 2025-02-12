
from function.imports import (
    pyperclip,
    pyautogui,
    time,
    click_and_fill,
    searchimage,
    copiar,
    FornecedorSelector
)


def empresa_principal(row):
        nome_fornecedor = copiar(row["Fornecedor"])
        print(nome_fornecedor.lower())
        selector = FornecedorSelector(nome_fornecedor.lower()).get_fornecedor()
        print("Esse é o selector: ", selector)
        time.sleep(2)
        searchimage('empresaPrincipal', 'empresaPrincipal Encontrado!', ' empresaPrincipal não encontrado!')
        searchimage('Entidade', 'entidade Encontrado!', 'entidade não encontrado!')
        pyperclip.copy(selector)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(7)
        click_and_fill('empresa', 'caminho empresa encontrada', 'empresa não encontrada')
        time.sleep(5)

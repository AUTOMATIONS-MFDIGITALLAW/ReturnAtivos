from function.imports import (
    pya,
    time,
    click_and_fill,
    searchimage,
)


def adverso_principal(row):
        searchimage('adversoprincipal', 'adversoprincipal Encontrado!', 'adversoprincipal não encontrado!')
        time.sleep(1)
        searchimage('Entidade', 'entidade Encontrado!', 'entidade não encontrado!')
        pya.write(row['Cpf/Cnpj'])
        time.sleep(3)
        click_and_fill('selecionar', 'caminho selecionar encontrado', 'caminho selecionar não encontrado')
        time.sleep(2)
        time.sleep(2)
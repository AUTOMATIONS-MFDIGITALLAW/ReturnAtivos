from function.imports import (
    time,
    desdobramento,
    cadastro,
    WebDriverManager,
    dados_gerais,
    empresa_principal,
    adverso_principal,
    search_image_time,
    advogados,
    info_finance,
    costumizados,
    object,
    eventos,
    eventosPrazo,
    documentos,
    chaves,
    requisicoes,
    buscar_pasta,
    pyautogui,
    copiar,
    click_and_fill
)
from function.logger import log

def etapa_processo(df):
    time.sleep(5)
    for index, row in df.iterrows():
        buscar_pasta()
        log.info('cadastro do procon iniciado!')
        dados_gerais(row)
        empresa_principal(row)
        adverso_principal(row)
        if search_image_time('ok','ok encontrado', 'ok não encontrado!'):
            log.success('Cliente já existente')
        else:
            time.sleep(2)
            log.success('Cadastro rapido iniciado!')
            cadastro(row)
        desdobramento(row)
        advogados()
        info_finance()
        costumizados(row)
        time.sleep(10)
        object()
        time.sleep(10)
        eventos()
        time.sleep(5)
        eventosPrazo()
        time.sleep(6)
        chaves()
        #requisicoes(row)
        time.sleep(10)
        click_and_fill('fechar', 'fechar encontrado!', 'fechar não encontrado')
        log.info('Cadastro completo: ' + row['Autor'])
        #é pra vim documentos agr
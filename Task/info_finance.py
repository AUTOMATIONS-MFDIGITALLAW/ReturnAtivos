from function.imports import (
    pya,
    time,
    endpoints,
    searchimage,
)

url = endpoints['TRI']

def info_finance():
    time.sleep(2)
    searchimage('infofinance', 'infofinance encontrado!', 'infofinance não encontrado!')
    time.sleep(2)
    searchimage('neutro','neutro encontrado', 'neutro não encontrado')
    searchimage('provisionar','provisionar encontrado','provisionar não encontrado')
    searchimage('valordacausa','valordacausa encontrado', 'valordacausa não encontrado')
    time.sleep(1)
    pya.write('0')
    time.sleep(1)







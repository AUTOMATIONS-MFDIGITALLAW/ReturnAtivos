import re
from logging import exception

import pandas as pd
import pyperclip
from tkinter import filedialog
import pyautogui as pya
from datetime import datetime, timedelta
from function.logger import log


def ler_arquivo():
    return filedialog.askopenfilename(title="Selecione o arquivo BASE DE DEVEDORES",filetypes=[("Arquivos Excel", "*.xlsx *.xls")])





def copiar(valor: str, date: bool = False, time: bool = False):
    try:
        if date and not time:
            valor = pd.to_datetime(valor, format='%d/%m/%Y', errors='coerce')
            valor = valor.strftime('%d/%m/%Y')

        if time and not date:
            valor = pd.to_datetime(valor, format='%H:%M:%S', errors='coerce')
            valor = valor.strftime('%H:%M:%S')

        if pd.notnull(valor):
            valor_final = str(valor)
            pyperclip.copy(valor_final)
            log.success('Valor Copiado!')
            return valor_final

    except Exception as e:
        log.error(f"Erro ao copiar valor: {e}")
        return None

    except exception as e:
        log.success('Valor não copiado!')



def extrair_comarca(foro):
    match = re.search(r'Procon Municipal de (.*?) - [A-Z]{2}$', foro.strip())
    match2 = re.search(r'Procon Estadual do (.*?) - [A-Z]{2}$', foro.strip())
    match3 = re.search(r'Procon Estadual de (.*?) - [A-Z]{2}$', foro.strip())
    match4 = re.search(r'Procon Estadual da (.*?) - [A-Z]{2}$', foro.strip())

    if match:
        log.success('Comarca com "Municipal de" encontrada')
        return match.group(1)
    if match2:
        log.success('Comarca com "estadual do" encontrada')
        return match2.group(1)
    if match3:
        log.success('Comarca com "estadual de" encontrada')
        return match3.group(1)
    if match4:
        log.success('Comarca com "estadual da" encontrada')
        return match4.group(1)

    else:
        log.critical('comarca sigla não compativel ou nome diferente da planilha!')


def date_dois_dias(i: int):
    current_date = datetime.now()
    new_date = current_date + timedelta(days=i)
    formatted_date = new_date.strftime('%d/%m/%Y')
    pyperclip.copy(formatted_date)
    return formatted_date



import pandas as pd
import pyperclip
from loguru import logger as log  # Certifique-se de que `loguru` está instalado

def copiar2(valor):
    try:
        if isinstance(valor, pd.Timestamp):
            valor = valor.strftime('%d/%m/%Y')

        elif isinstance(valor, str):
            valor = pd.to_datetime(valor, errors='coerce')
            if pd.notnull(valor):
                valor = valor.strftime('%d/%m/%Y')

        if pd.notnull(valor):
            pyperclip.copy(valor)
            log.success('Valor Copiado!')
            return valor
        else:
            log.warning('Valor é nulo, nada copiado.')
            return None

    except Exception as e:
        log.error(f"Erro ao copiar valor: {e}")
        return None

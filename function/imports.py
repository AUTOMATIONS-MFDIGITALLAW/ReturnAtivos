
import time

import pyautogui
import pyautogui as pya
import pyperclip
import datetime

from end import endpoints
from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage, search_image_time
from function.read_dataframe import copiar, copiar2, extrair_comarca, date_dois_dias
from function.fornecedor import FornecedorSelector, CreditoSelector
from function.webdriver import WebDriverManager
from Task.desdobramento import desdobramento
from Task.cadastro import cadastro
from Task.dados_gerais import dados_gerais
from Task.advogados import advogados
from Task.info_finance import info_finance
from Task.costumizados import costumizados
from Task.eventos import eventos, eventosPrazo
from Task.documentos import documentos
from Task.chaves import chaves
from Task.object import object
from Task.requisicoes import requisicoes
from Task.buscar_pasta import buscar_pasta
from Task.adverso_principal import adverso_principal
from Task.empresa_principal import empresa_principal



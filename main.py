import flet as ft
from end import endpoints
import os
from Task.login import logar
from Task.process import etapa_processo
from function.read_dataframe import ler_arquivo
import pandas as pd
from function.logger import log
from function.config import load_environment


load_environment()
usern = os.getenv('USERN')
passw = os.getenv('SENHA')
url = endpoints['TRI']


import sys
from pathlib import Path


if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).parent


img_path = base_path / "img"
function_path = base_path / "function"
src_path = base_path / "src"
task_path = base_path / "Task"




def main(page: ft.Page):
    page.title = "Automação do PROCON"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    log.info('automação iniciada')

    df = None


    def importar(e):
        nonlocal df
        try:
            file_path = ler_arquivo()
            df = pd.read_excel(file_path, dtype=str)
            log.success('Planilha Importada: ' + file_path),
            page.add(ft.Text("Importação concluída com sucesso!", size=20, color=ft.colors.GREEN))
        except Exception as ex:
            log.warning('error ao importar planilha: ' + file_path),
            page.add(ft.Text("Erro na importação", size=20, color=ft.colors.RED))


    def iniciar_automacao(e):
        if df is None:
            log.info('Nenhuma Planilha foi importada!')
            page.add(ft.Text('Nenhuma Planilha foi importada!', size=20, color=ft.colors.RED))
            return
        try:
            logar(url, usern, passw)
            etapa_processo(df)
            page.add(ft.Text(log.success('automação iniciada!'), size=20, color=ft.colors.GREEN))
        except Exception as ex:
            page.add(ft.Text(log.critical('Error na automação'), size=20, color=ft.colors.RED))


    def sair(e):
        log.info("Automação fechada")
        os._exit(0)  # Encerra o processo imediatamente


    page.add(
        ft.Column(
            [
                ft.Text(
                    "Bem-vindo à Automação do PROCON",
                    size=30,
                    weight="bold",
                    font_family="Arial Black",
                ),
                ft.ElevatedButton("Importar Planilha", on_click=importar),
                ft.ElevatedButton("Iniciar Automação", on_click=iniciar_automacao),
                ft.ElevatedButton("Sair", on_click=sair),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)




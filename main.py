import flet as ft
from end import endpoints
import os
from Task.login import logar
from Task.process import etapa_processo
from function.read_dataframe import ler_arquivo
from function.selecionar_pasta import selecionar_pasta_pdfs  # Importação correta
from Task.documentos import documentos  # Agora usamos essa função corretamente
import pandas as pd
from function.logger import log
from function.config import load_environment
import glob  # Para listar arquivos PDF

load_environment()
url = endpoints['TRI']


def main(page: ft.Page):
    page.title = "Cadastro - Return&Ativos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    log.info('Automação iniciada')

    df = None
    pasta_pdfs = None  # Caminho da pasta onde estão os PDFs

    user_input = ft.TextField(label="Usuário", width=300)
    pass_input = ft.TextField(label="Senha", password=True, width=300)

    def importar(e):
        nonlocal df
        try:
            file_path = ler_arquivo()
            df = pd.read_excel(file_path, dtype=str)
            log.success(f'Planilha Importada: {file_path}')
            page.add(ft.Text("Importação concluída com sucesso!", size=20, color=ft.colors.GREEN))
        except Exception as ex:
            log.warning(f'Erro ao importar planilha: {ex}')
            page.add(ft.Text("Erro na importação", size=20, color=ft.colors.RED))

    def selecionar_pasta(e):
        """ Permite selecionar uma pasta onde estão os PDFs """
        nonlocal pasta_pdfs
        pasta_pdfs = selecionar_pasta_pdfs()
        if pasta_pdfs:
            page.add(ft.Text(f"Pasta selecionada: {pasta_pdfs}", size=18, color=ft.colors.BLUE))

    def listar_pdfs(e):
        """ Lista os PDFs dentro da pasta selecionada """
        if pasta_pdfs:
            pdf_files = glob.glob(os.path.join(pasta_pdfs, "*.pdf"))
            if pdf_files:
                log.success(f"Encontrados {len(pdf_files)} arquivos PDF na pasta: {pasta_pdfs}")

                # Log detalhado de cada PDF encontrado
                for pdf in pdf_files:
                    log.info(f"PDF encontrado: {pdf}")

                # Exibição na interface gráfica
                page.add(ft.Text(f"Total de PDFs encontrados: {len(pdf_files)}", size=18, color=ft.colors.GREEN))
                for pdf in pdf_files:
                    page.add(ft.Text(f"Arquivo: {os.path.basename(pdf)}", size=16, color=ft.colors.BLACK))
            else:
                log.warning("Nenhum PDF encontrado")
                page.add(ft.Text("Nenhum arquivo PDF encontrado na pasta!", size=16, color=ft.colors.RED))
        else:
            log.warning("Nenhuma pasta de PDFs foi selecionada")
            page.add(ft.Text("Nenhuma pasta de PDFs foi selecionada!", size=16, color=ft.colors.RED))

    def iniciar_automacao(e):
        """ Inicia a automação após validar login, planilha e PDF """
        nonlocal df
        usern = user_input.value.strip()
        passw = pass_input.value.strip()

        if not usern or not passw:
            log.warning('Usuário e senha devem ser preenchidos!')
            page.add(ft.Text('Preencha o usuário e a senha antes de iniciar!', size=20, color=ft.colors.RED))
            return

        if df is None:
            log.info('Nenhuma Planilha foi importada!')
            page.add(ft.Text('Nenhuma Planilha foi importada!', size=20, color=ft.colors.RED))
            return

        if not pasta_pdfs:
            log.warning("Nenhuma pasta de PDFs foi selecionada!")
            page.add(ft.Text("Selecione uma pasta antes de iniciar!", size=20, color=ft.colors.RED))
            return

        try:
            log.info(f"Iniciando automação para o usuário: {usern}")
            logar(url, usern, passw)
            etapa_processo(df)

            # Passar a pasta para a função documentos()
            documentos(pasta_pdfs)

            page.add(ft.Text("Automação iniciada com sucesso!", size=20, color=ft.colors.GREEN))
        except Exception as ex:
            log.critical(f"Erro na automação: {ex}")
            page.add(ft.Text("Erro na automação", size=20, color=ft.colors.RED))

    def sair(e):
        log.info("Automação fechada")
        os._exit(0)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Bem-vindo à Automação do PROCON",
                    size=30,
                    weight="bold",
                    font_family="Arial Black",
                ),
                user_input,
                pass_input,
                ft.ElevatedButton("Importar Planilha", on_click=importar),
                ft.ElevatedButton("Selecionar Pasta de PDFs", on_click=selecionar_pasta),
                ft.ElevatedButton("Listar PDFs na Pasta", on_click=listar_pdfs),
                ft.ElevatedButton("Iniciar Automação", on_click=iniciar_automacao),
                ft.ElevatedButton("Sair", on_click=sair),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)

import re
import pandas as pd
from PyPDF2 import PdfReader
from tkinter import Tk, filedialog


def selecionar_arquivo():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return file_path


def contar_paginas(reader):
    return min(2, len(reader.pages))  # Pegamos até 2 páginas


def extrair_texto(reader):
    """
    Extrai texto APENAS da primeira e segunda página do PDF.
    """
    textos = []
    num_paginas = contar_paginas(reader)

    for i in range(num_paginas):
        textos.append(reader.pages[i].extract_text())

    return textos


def extrair_nome_autor(texto_primeira_pagina):
    """
    Busca o Nome do Autor em toda a primeira página do PDF.
    - Se encontrar "Autor:", pega o nome após isso e antes da vírgula.
    - Se não encontrar "Autor:", pega o primeiro nome que antecede uma vírgula.
    """
    if not texto_primeira_pagina:
        return None

    # Buscar nome após "Autor:" e antes da vírgula
    match_autor = re.search(r"Autor:\s*([\wÀ-ÿ\s]+?),", texto_primeira_pagina, re.IGNORECASE)
    if match_autor:
        return match_autor.group(1).strip()

    # Caso não tenha "Autor:", pegar qualquer nome antes da vírgula
    match_nome = re.search(r"([\wÀ-ÿ\s]+?),", texto_primeira_pagina)
    if match_nome:
        return match_nome.group(1).strip()

    return None


def buscar_padroes(textos):
    """
    Busca CPFs, Datas e Processos dentro do texto do PDF.
    Remove processos duplicados.
    """
    processos_unicos = set()
    dados = []

    for text in textos:
        cpfs = re.findall(r"\d{3}\.\d{3}\.\d{3}-\d{2}", text)
        datas = re.findall(r"\d{2}/\d{2}/\d{4}", text)
        processos = re.findall(r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}", text)

        # Filtrar processos para evitar duplicatas
        processos = list(set(processos) - processos_unicos)
        processos_unicos.update(processos)

        dados.append({
            "CPF": ", ".join(cpfs) if cpfs else None,
            "Data de Citação": ", ".join(datas) if datas else None,
            "Processos": ", ".join(processos) if processos else None,
        })

    return dados


def buscar_uf_comarca(textos):
    """
    Busca a UF e Comarca a partir do formato "Cidade/UF".
    """
    dados = []

    for text in textos:
        padrao = r"([\wÀ-ÿ\s]+?)/([A-Z]{2})"

        for match in re.finditer(padrao, text):
            comarca = match.group(1).strip()
            uf = match.group(2)

            dados.append({
                "UF": uf,
                "Comarca": comarca,
            })

    return dados


def buscar_orgaos_judiciarios(textos):
    """
    Busca no texto as ocorrências de "Vara Cível da Comarca" e "Juizado Especial".
    """
    dados = []
    padroes = [
        r"Vara\s+C[ií]vel\s+da\s+Comarca",
        r"Juizado\s+Especial"
    ]

    for text in textos:
        for padrao in padroes:
            for match in re.finditer(padrao, text, re.IGNORECASE):
                dados.append({
                    "Órgão Judiciário": match.group()
                })

    return dados


def salvar_em_excel(nome_autor, dados_gerais, dados_uf_comarca, dados_orgaos):
    """
    Salva todas as informações extraídas em uma ÚNICA aba no Excel.
    """
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Planilha Excel", "*.xlsx")],
        title="Salvar arquivo Excel"
    )

    if file_path:
        # Criar um único DataFrame combinando todas as informações
        df_geral = pd.DataFrame(dados_gerais)
        df_uf_comarca = pd.DataFrame(dados_uf_comarca)
        df_orgaos = pd.DataFrame(dados_orgaos)

        # Adicionar a coluna "Nome do Autor"
        df_final = pd.concat([df_geral, df_uf_comarca, df_orgaos], axis=1)
        df_final.insert(0, "Nome do Autor", nome_autor)  # Inserir na primeira coluna

        # Salvar no Excel
        df_final.to_excel(file_path, sheet_name="Dados Extraídos", index=False)

        print(f"\n📊 Os dados foram salvos no arquivo: {file_path}")
    else:
        print("❌ O usuário cancelou o salvamento.")


def ler_pdf():
    """
    Realiza todo o processamento do PDF e salva os dados em Excel.
    """
    file_path = selecionar_arquivo()

    if file_path:
        with open(file_path, "rb") as file:
            reader = PdfReader(file)

            num_paginas = contar_paginas(reader)
            print(f"\n📑 O PDF possui {num_paginas} páginas.\n")

            textos = extrair_texto(reader)  # Pegamos só as 2 primeiras páginas

            nome_autor = extrair_nome_autor(textos[0])  # Busca nome do autor na 1ª página
            print(f"👤 Nome do Autor: {nome_autor}")

            dados_gerais = buscar_padroes(textos)
            dados_uf_comarca = buscar_uf_comarca(textos)
            dados_orgaos = buscar_orgaos_judiciarios(textos)

            salvar_em_excel(nome_autor, dados_gerais, dados_uf_comarca, dados_orgaos)

    else:
        print("❌ Nenhum arquivo selecionado.")


ler_pdf()

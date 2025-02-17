import os
import sys


def get_resource_path(relative_path):
   """Obter o caminho dos recursos para a execução no executável"""
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")
   return os.path.join(base_path, relative_path)

IMG = {
    'cookie': get_resource_path('img/cookie.png'),
    'incluir_processo': get_resource_path('img/incluir_processo.png'),
    'processo': get_resource_path('img/processo.png'),
    'natureza': get_resource_path('img/natureza.png'),
    'TipoAcao': get_resource_path('img/TipoAcao.png'),
    'procedimento': get_resource_path('img/procedimento.png'),
    'administrativo': get_resource_path('img/administrativo.png'),
    'unidadeOrganizacional': get_resource_path('img/UnidadeOrga.png'),
    'unidadeCentral': get_resource_path('img/UnidadeOrgaCentral.png'),
    'admProcess': get_resource_path('img/admProcess.png'),
    'Nota': get_resource_path('img/Nota.png'),
    'empresaPrincipal': get_resource_path('img/EmpresaPrincipal.png'),
    'Entidade': get_resource_path('img/Entidade.png'),
    'adversoprincipal': get_resource_path('img/adversoprincipal.png'),
    'tipodepessoa': get_resource_path('img/TipoDePessoa.png'),
    'tipodedocumento': get_resource_path('img/TipoDeDocumento.png'),
    'cadastrorapido': get_resource_path('img/cadastrorapido.png'),
    'numerododocumento': get_resource_path('img/numerododocumento.png'),
    'salvar': get_resource_path('img/salvar.png'),
    'entidadevazia': get_resource_path('img/EntidadeVazia.png'),
    'ok': get_resource_path('img/OK.png'),
    'desdobramento': get_resource_path('img/desdobramento.png'),
    'numerodoprocesso': get_resource_path('img/numerodoprocesso.png'),
    'tipodedesdobramento': get_resource_path('img/tipodedesdobramento.png'),
    'Tribunal': get_resource_path('img/Tribunal.png'),
    'juris': get_resource_path('img/juris.png'),
    'UF': get_resource_path('img/UF.png'),
    'comarca': get_resource_path('img/comarca.png'),
    'advogados': get_resource_path('img/advogados.png'),
    'semadv': get_resource_path('img/SemAdvogado.png'),
    'setadireita': get_resource_path('img/SetaDireita.png'),
    'setadireita2': get_resource_path('img/SetaDireita2.png'),
    'meirelestribanco': get_resource_path('img/MeirelesTribanco.png'),
    'infofinance': get_resource_path('img/infofinance.png'),
    'neutro': get_resource_path('img/Neutro.png'),
    'provisionar': get_resource_path('img/provisionar.png'),
    'valordacausa': get_resource_path('img/valordacausa.png'),
    'costumizados': get_resource_path('img/costumizados.png'),
    'datadecaptura': get_resource_path('img/datacaptura.png'),
    'cedido': get_resource_path('img/cedido.png'),
    'classpos': get_resource_path('img/classpos.png'),
    'objetos': get_resource_path('img/objetos.png'),
    'adicionar': get_resource_path('img/adicionar.png'),
    'metodoatt': get_resource_path('img/metodoAtt.png'),
    'eventos': get_resource_path('img/eventos.png'),
    'selecioneevento': get_resource_path('img/selecioneEvento.png'),
    'modalidade': get_resource_path('img/modalidade.png'),
    'relevante': get_resource_path('img/relevante.png'),
    'andamento': get_resource_path('img/andamento.png'),
    'objetoselecionar': get_resource_path('img/objetoselecionar.png'),
    'abripasta': get_resource_path('img/abripasta.png'),
    'okamarelo': get_resource_path('img/okamarelo.png'),
    'dataeventos': get_resource_path('img/dataeventos.png'),
    'detalhes': get_resource_path('img/detalhes.png'),
    'encaminhamento': get_resource_path('img/encaminhamento.png'),
    'ludimila': get_resource_path('img/ludimila.png'),
    'jone': get_resource_path('img/jone.png'),
    'Apresentar': get_resource_path('img/Apresentar.png'),
    'Lembrete': get_resource_path('img/Lembrete.png'),
    'Dias': get_resource_path('img/Dias.png'),
    'documentos': get_resource_path('img/documentos.png'),
    'palavraschaves': get_resource_path('img/palavraschaves.png'),
    'requisicoes': get_resource_path('img/requisicoes.png'),
    'titulo': get_resource_path('img/titulo.png'),
    'tipoderequisicao': get_resource_path('img/tipoderequisicao.png'),
    'responsavelexecutado': get_resource_path('img/responsavelexecutado.png'),
    'detalhesrequisicao': get_resource_path('img/detalhesrequisicao.png'),
    'unidadeorga': get_resource_path('img/unidadeorga2.png'),
    'seta3': get_resource_path('img/seta3.png'),
    'setadupla': get_resource_path('img/setadupla.png'),
    'CNJ': get_resource_path('img/CNJ.png'),
    'Responsavel': get_resource_path('img/Responsavel.png'),
    'classpre': get_resource_path('img/classpre.png'),
    'Laura': get_resource_path('img/Laura.png'),
    'Lais': get_resource_path('img/Lais.png'),
    'Requisitante': get_resource_path('img/Requisitante.png'),
}

POSITION = {
   'cookie': (1767, 972),
   'processo': (68, 317),
   'data da citacao': (775,489),
   'subir': (888, 465),
   'tri': (975,634),
   'vazio': (766,621),
   'vazio2': (668, 687),
   'selecionar': (525,546),
   'buscaadv': (574, 519),
   'buscaempresa': (589, 584),
   'empresa':(582, 506),
   'eventos': (635, 495),
   'data da citacao2': (1004, 464),
   'procon': (704, 479),
   'procon2':(572,564),
   'requisicao':(617,581),
   'fechar': (638, 247)
}

from function.imports import (
    time,
    pya,
    pyperclip,
    pyautogui,
    searchimage,
    date_dois_dias,
    datetime,
    copiar,
    click_and_fill
)

def eventos():
    searchimage('eventos','eventos encontrado','eventos não encontrado')
    time.sleep(5)
    searchimage('adicionar', 'adiconar encontrado', 'adicionar não encontrado')
    time.sleep(2)
    searchimage('dataeventos','dataeventos encontrado','dataeventos não encontrado')
    date_dois_dias(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('relevante','relevante encontrado!', 'relevante não encontrado')
    searchimage('andamento','andamento encontrado!', 'andamento não encontrado')
    time.sleep(3)
    searchimage('selecioneevento','selecioneevento encontrado!', 'selecioneevento não encontrado')
    time.sleep(3)
    texto = 'INFORMAÇÕES ADICIONAIS PARA ANÁLISE - PROCON'
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(6)
    click_and_fill('data da citacao','caminho vazio encontrado', 'Caminho vazio não encontrado') #clique aleatorio
    click_and_fill('data da citacao','caminho vazio encontrado', 'Caminho vazio não encontrado') #clique aleatorio
    searchimage('modalidade','modalidade encontrada', 'modalidade não encontrado')
    time.sleep(4)
    texto = "Não Se Aplica"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('detalhes','detalhes encontrada', 'detalhes não encontrado')
    texto = 'Prezados, Por gentileza, encaminhar informações adicionais, caso necessário: Faturas/Vision/Dados do Lojista/Recupera; Data emissão Cartão e ano cessão.'
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('encaminhamento', 'encaminhamento encontrada', 'encaminhamento não encontrado')
    time.sleep(10)

    click_and_fill('eventos','caminho eventos encontrado', 'Caminho eventos não encontrado')
    pya.write('Ludimila gon')
    searchimage('ludimila', 'ludimila ancontrada', 'ludimila não encontrada')
    time.sleep(4)
    searchimage('setadireita2', 'setadireita ancontrada', 'seta não encontrada')
    click_and_fill('eventos','caminho eventos encontrado', 'Caminho eventos não encontrado')
    pya.write('LAURA CRISTINA BORGES MARTINS')
    searchimage('Laura', 'Laura ancontrada', 'Laura não encontrada')
    time.sleep(4)
    searchimage('setadireita2', 'setadireita ancontrada', 'seta não encontrada')
    pyautogui.scroll(-800)
    time.sleep(4)
    searchimage('Apresentar', 'Apresentar encontrada', 'Apresentar não encontrado')
    searchimage('Lembrete', 'Lembrete encontrada', 'Lembrete não encontrado')
    time.sleep(2)
    searchimage('Dias', 'Dias encontrada', 'Dias não encontrado')
    time.sleep(2)
    pya.write('999')
    searchimage('salvar','salvar encontrado','salvar não encontrado')


#Prazo
def eventosPrazo():
    searchimage('eventos','eventos encontrado','eventos não encontrado')
    time.sleep(5)
    searchimage('adicionar', 'adiconar encontrado', 'adicionar não encontrado')
    time.sleep(5)
    searchimage('dataeventos','dataeventos encontrado','dataeventos não encontrado')
    date_dois_dias(10)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('relevante','relevante encontrado!', 'relevante não encontrado')
    searchimage('andamento','andamento encontrado!', 'andamento não encontrado')
    time.sleep(3)
    searchimage('selecioneevento','selecioneevento encontrado!', 'selecioneevento não encontrado')
    time.sleep(3)
    texto = 'Orientações e Subsídios ao Cessionário'
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(6)
    click_and_fill('data da citacao','caminho vazio encontrado', 'Caminho vazio não encontrado')  # clique aleatorio
    time.sleep(3)
    searchimage('modalidade','modalidade encontrada', 'modalidade não encontrado')
    time.sleep(4)
    texto = "Não Se Aplica"
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    time.sleep(3)
    searchimage('detalhes', 'detalhes encontrada', 'detalhes não encontrado')
    texto = 'Gentileza encaminhar os subsidios'
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    searchimage('encaminhamento', 'encaminhamento encontrada', 'encaminhamento não encontrado')
    time.sleep(2)
    click_and_fill('eventos', 'caminho eventos encontrado', 'Caminho eventos não encontrado')
    pya.write(' LAÍS MORESCHI (Matheus Fernandes)')
    searchimage('Lais', 'Lais ancontrada', 'Lais não encontrada')
    time.sleep(4)
    searchimage('setadireita2', 'setadireita ancontrada', 'seta não encontrada')
    pyautogui.scroll(-1000)
    time.sleep(6)
    searchimage('Apresentar', 'Apresentar encontrada', 'Apresentar não encontrado')
    searchimage('Lembrete', 'Lembrete encontrada', 'Lembrete não encontrado')
    searchimage('Dias', 'Dias encontrada', 'Dias não encontrado')
    time.sleep(2)
    pya.write('999')
    searchimage('salvar', 'salvar encontrado', 'salvar não encontrado')
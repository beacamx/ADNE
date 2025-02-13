import csv
import os
from utils import mes_nome
from membros import carregar_membros
from membros import encontrar_membros_por_nome
from membros import escolher_membro

def carregar_dados_mes_ano(mes, ano):
    # Define o caminho para a pasta do mês
    caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
    
    # Verifica se a pasta existe
    if not os.path.exists(caminho_pasta):
        print(f"⚠️ Pasta do mês {mes:02d} não encontrada.")
        return None
    
    # Carrega os arquivos CSV
    dados = {}
    for arquivo in ["presencas.csv", "faltas.csv", "cultos_cancelados.csv"]:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as f:
                dados[arquivo] = list(csv.reader(f))
        else:
            print(f"⚠️ Arquivo {arquivo} não encontrado no mês {mes:02d}.")
            dados[arquivo] = None
    
    return dados

def registrar_presenca():
    data = input("Data do culto (YYYY-MM-DD): ")
    nome = input("Nome do membro: ")
    funcao = input("Função desempenhada: ")
    observacao = input("Observação (se houver): ")
    
    nome = nome.strip().title()
    funcao = funcao.strip().title()
    observacao = observacao.capitalize()
    
    # Extrai o ano e o mês da data
    try:
        ano, mes, _ = data.split('-')
        mes = int(mes)
        ano = int(ano)
    except ValueError:
        print("⚠️ Formato de data inválido. Use YYYY-MM-DD.")
        return
    
    # Verifica se o membro existe no arquivo geral de membros
    membros = carregar_membros()
    if not membros:
        print("⚠️ Não foi possível carregar o arquivo de membros.")
        return
    
    # Verifica se o membro existe usando a função encontrar_membros_por_nome
    membros_encontrados = encontrar_membros_por_nome(nome, membros)
    
    if not membros_encontrados:
        print(f"⚠️ Membro '{nome}' não encontrado no arquivo de membros.")
        return
    
    # Permite ao usuário escolher um membro, se houver mais de um
    membro_escolhido = escolher_membro(membros_encontrados)
    if not membro_escolhido:
        return  # Se a escolha for inválida, cancela a operação
    
    # Carrega os dados do mês/ano (para verificar se a pasta/arquivo existe)
    dados_mes = carregar_dados_mes_ano(mes, ano)
    if dados_mes is None:
        print(f"⚠️ Não foi possível carregar os dados do mês {mes:02d}/{ano}.")
        return
    
    # Define o caminho para a pasta do mês
    caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
    
    # Caminho para o arquivo de presenças do mês
    caminho_presencas = os.path.join(caminho_pasta, "presencas.csv")
    
    # Verifica se o arquivo de presenças já existe
    arquivo_existe = os.path.exists(caminho_presencas)
    
    # Abre o arquivo para adicionar a nova presença
    with open(caminho_presencas, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Se o arquivo não existir, escreve o cabeçalho
        if not arquivo_existe:
            writer.writerow(["Data", "Nome", "Função", "Observação"])
        
        # Escreve a nova presença
        writer.writerow([data, membro_escolhido[0], funcao, observacao])
    
    print("Presença registrada com sucesso!")

def registrar_falta():
    data = input("Data do culto (YYYY-MM-DD): ")
    nome = input("Nome do membro: ")
    nome = nome.strip().title()
    funcao = input("Função que iria desempenhar: ")
    justificativa = input("Justificativa: ")
    
    # Extrai o ano e o mês da data
    try:
        ano, mes, _ = data.split('-')
        mes = int(mes)
        ano = int(ano)
    except ValueError:
        print("⚠️ Formato de data inválido. Use YYYY-MM-DD.")
        return
    
    # Carrega o arquivo de membros
    membros = carregar_membros()
    if not membros:
        print("⚠️ Não foi possível carregar o arquivo de membros.")
        return
    
    # Verifica se o membro existe usando a função encontrar_membros_por_nome
    membros_encontrados = encontrar_membros_por_nome(nome, membros)
    
    if not membros_encontrados:
        print(f"⚠️ Membro '{nome}' não encontrado no arquivo de membros.")
        return
    
    # Permite ao usuário escolher um membro, se houver mais de um
    membro_escolhido = escolher_membro(membros_encontrados)
    if not membro_escolhido:
        return  # Se a escolha for inválida, cancela a operação
    
    # Carrega os dados do mês/ano (para verificar se a pasta/arquivo existe)
    dados_mes = carregar_dados_mes_ano(mes, ano)
    if dados_mes is None:
        print(f"⚠️ Não foi possível carregar os dados do mês {mes:02d}/{ano}.")
        return
    
    # Define o caminho para a pasta do mês
    caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
    
    # Caminho para o arquivo de faltas do mês
    caminho_faltas = os.path.join(caminho_pasta, "faltas.csv")
    
    # Verifica se o arquivo de faltas já existe
    arquivo_existe = os.path.exists(caminho_faltas)
    
    # Abre o arquivo para adicionar a nova falta
    with open(caminho_faltas, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Se o arquivo não existir, escreve o cabeçalho
        if not arquivo_existe:
            writer.writerow(["Data", "Nome", "Função", "Justificativa"])
        
        # Escreve a nova falta
        writer.writerow([data, membro_escolhido[0], funcao, justificativa])
    
    print("Falta registrada com sucesso!")

def registrar_culto_cancelado():
    data = input("Data do culto cancelado (YYYY-MM-DD): ")
    motivo = input("Motivo do cancelamento: ")
    
    # Extrai o ano e o mês da data
    try:
        ano, mes, _ = data.split('-')
        mes = int(mes)
        ano = int(ano)
    except ValueError:
        print("⚠️ Formato de data inválido. Use YYYY-MM-DD.")
        return
    
    # Define o caminho para a pasta do mês
    caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
    
    # Verifica se a pasta existe; se não, cria a pasta
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    # Caminho para o arquivo de cultos cancelados do mês
    caminho_cultos_cancelados = os.path.join(caminho_pasta, "cultos_cancelados.csv")
    
    # Verifica se o arquivo de cultos cancelados já existe
    arquivo_existe = os.path.exists(caminho_cultos_cancelados)
    
    # Abre o arquivo para adicionar o novo registro
    with open(caminho_cultos_cancelados, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Se o arquivo não existir, escreve o cabeçalho
        if not arquivo_existe:
            writer.writerow(["Data", "Motivo"])
        
        # Escreve o novo registro
        writer.writerow([data, motivo])
    
    print("Culto cancelado registrado com sucesso!")
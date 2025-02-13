import csv
import os
import matplotlib.pyplot as plt
from collections import Counter

CAMINHO_MEMBROS = "./dados/membros.csv"

def adicionar_membro():
    nome = input("Nome do membro: ")
    ano_entrada = input("Ano de entrada (exemplo: 2025): ")
    funcoes = input("Funções (separadas por vírgula): ")
    ativo = "Sim"
    
    # Padronização das variáveis
    nome = nome.strip().title() # Deixa a primeira letra do nome e do sobrenome em maiúsculo pra manter um padrão
    funcoes = ', '.join([funcao.strip().title() for funcao in funcoes.split(',')])
    
    # Verifica se o arquivo existe, se não, cria com o cabeçalho
    if not os.path.exists(CAMINHO_MEMBROS):
        with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Ano de Entrada", "Funções", "Ativo"])
    
    # Adiciona o novo membro
    with open(CAMINHO_MEMBROS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, ano_entrada, funcoes, ativo])
    print("Membro adicionado com sucesso!")
    
def atualizar_membro():
    print("1. Alterar nome")
    print("2. Alterar ano de entrada")
    print("3. Alterar função(ões)")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        alterar_nome_membro()
    elif opcao == '2':
        alterar_ano_entrada_membro()
    elif opcao == '3':
        alterar_funcoes_membro()

def encontrar_membros_por_nome(nome, membros):
    """
    Busca membros pelo nome completo ou pelo primeiro nome.
    
    :param nome: Nome digitado pelo usuário (pode ser nome completo ou apenas o primeiro nome).
    :param membros: Lista de membros lida do arquivo CSV.
    :return: Lista de membros que correspondem ao nome digitado.
    """
    membros_encontrados = []
    nome = nome.strip().title()  # Padroniza o nome para busca
    
    for linha in membros[1:]:  # Ignora o cabeçalho
        nome_completo = linha[0].strip().title()
        primeiro_nome = nome_completo.split()[0]
        
        # Verifica se o nome digitado corresponde ao nome completo ou ao primeiro nome
        if nome == nome_completo or nome == primeiro_nome:
            membros_encontrados.append(linha)
    
    return membros_encontrados

def escolher_membro(membros_encontrados):
    """
    Permite ao usuário escolher um membro entre vários encontrados.
    
    :param membros_encontrados: Lista de membros encontrados.
    :return: O membro escolhido pelo usuário.
    """
    if len(membros_encontrados) > 1:
        print("\nForam encontrados vários membros com esse nome. Escolha qual deseja atualizar:")
        for i, membro in enumerate(membros_encontrados, start=1):
            print(f"{i}. {membro[0]} (Ano de entrada: {membro[1]}, Funções: {membro[2]}, Ativo: {membro[3]})")
        
        escolha = input("Digite o número correspondente ao membro que deseja atualizar: ")
        try:
            escolha = int(escolha) - 1  # Converte para índice
            if escolha < 0 or escolha >= len(membros_encontrados):
                print("⚠️ Escolha inválida. Operação cancelada.")
                return None
            return membros_encontrados[escolha]
        except ValueError:
            print("⚠️ Entrada inválida. Operação cancelada.")
            return None
    else:
        return membros_encontrados[0]
    
def alterar_nome_membro():
    nome = input("Nome do membro a ser alterado: ")
    
    # Verifica se o arquivo existe, se não, cria com o cabeçalho
    if not os.path.exists(CAMINHO_MEMBROS):
        with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Ano de Entrada", "Funções", "Ativo"])
    
    # Adiciona o novo membro
    with open(CAMINHO_MEMBROS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        membros = list(reader)
    
    # Busca membros pelo nome digitado
    membros_encontrados = encontrar_membros_por_nome(nome, membros)
    
    if not membros_encontrados:
        print("⚠️ Membro não encontrado. Verifique o nome e tente novamente.")
        return
    
    # Permite ao usuário escolher um membro, se houver mais de um
    membro_escolhido = escolher_membro(membros_encontrados)
    if not membro_escolhido:
        return  # Se a escolha for inválida, cancela a operação
    
    # Solicita o nome atualizado
    nomeAtualizado = input("Nome do membro atualizado: ")
    nomeAtualizado = nomeAtualizado.strip().title()  # Padroniza o nome atualizado
    
    # Atualiza o nome no CSV
    with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(membros[0])  # Escreve o cabeçalho
        for linha in membros[1:]:
            if linha == membro_escolhido:
                linha[0] = nomeAtualizado  # Atualiza o nome
            writer.writerow(linha)
    
    print("Nome atualizado com sucesso!")

def alterar_ano_entrada_membro():
    nome = input("Nome do membro a ser alterado: ")
    
    with open(CAMINHO_MEMBROS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        membros = list(reader)
    
    # Busca membros pelo nome digitado
    membros_encontrados = encontrar_membros_por_nome(nome, membros)
    
    if not membros_encontrados:
        print("⚠️ Membro não encontrado. Verifique o nome e tente novamente.")
        return
    
    # Permite ao usuário escolher um membro, se houver mais de um
    membro_escolhido = escolher_membro(membros_encontrados)
    if not membro_escolhido:
        return  # Se a escolha for inválida, cancela a operação
    
    # Solicita o novo ano de entrada
    anoEntradaAtualizado = input("Ano de entrada atualizado (exemplo: 2025): ")
    
    # Atualiza o ano de entrada no CSV
    with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(membros[0])  # Escreve o cabeçalho
        for linha in membros[1:]:
            if linha == membro_escolhido:
                linha[1] = anoEntradaAtualizado  # Atualiza o ano de entrada
            writer.writerow(linha)
    
    print("Ano de entrada atualizado com sucesso!")
    
def alterar_funcoes_membro():
    nome = input("Nome do membro a ser alterado: ")
    nome = nome.strip().title()  # Padroniza o nome para busca
    
    with open(CAMINHO_MEMBROS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        membros = list(reader)
    
    # Busca membros pelo nome digitado
    membros_encontrados = encontrar_membros_por_nome(nome, membros)
    
    if not membros_encontrados:
        print("⚠️ Membro não encontrado. Verifique o nome e tente novamente.")
        return
    
    # Permite ao usuário escolher um membro, se houver mais de um
    membro_escolhido = escolher_membro(membros_encontrados)
    if not membro_escolhido:
        return  # Se a escolha for inválida, cancela a operação
    
    funcoesAtualizadas = input("Funções atualizadas (separadas por vírgula): ")
    funcoesAtualizadas = ', '.join([funcao.strip().title() for funcao in funcoesAtualizadas.split(',')])  # Padroniza as funções atualizadas
    
    # Atualiza o nome no CSV
    with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(membros[0])  # Escreve o cabeçalho
        for linha in membros[1:]:
            if linha == membro_escolhido:
                linha[2] = funcoesAtualizadas  # Atualiza as funções
            writer.writerow(linha)
    
    print("Funções atualizadas com sucesso!")  
    
def plotar_grafico_funcoes(funcoes):
    contagem_funcoes = Counter(funcoes)
    labels = list(contagem_funcoes.keys())
    valores = list(contagem_funcoes.values())
    
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho do gráfico
    bars = plt.bar(labels, valores, color='blue')
    
    # Adiciona os valores exatos no topo de cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', 
                 ha='center', va='bottom', fontsize=10)
    
    plt.xlabel("Funções", fontsize=12)
    plt.ylabel("Quantidade de Membros", fontsize=12)
    plt.title("Distribuição de Membros por Função", fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotaciona os rótulos do eixo X para melhor legibilidade
    plt.yticks(fontsize=10)
    plt.tight_layout()  # Ajusta o layout para evitar cortes
    plt.show()
    
def visualizar_membros():
    try:
        with open(CAMINHO_MEMBROS, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            membros = list(reader)
            
            if not membros or len(membros) == 1:  # Verifica se só tem o cabeçalho
                print("Nenhum membro cadastrado.")
                return
            
            print("\nLista de Membros:")
            print(f"{'Nome':<20} {'Data de Entrada':<15} {'Funções':<30} {'Ativo':<10}")
            print("-" * 75)
            
            funcoes = []
            for linha in membros[1:]:
                if len(linha) < 4:  # Garante que há pelo menos 4 colunas antes de processar
                    print(f"⚠️ Linha inválida ignorada: {linha}")  # Depuração
                    continue
                nome, data_entrada, funcoes_membro, ativo = linha[:4]  # Pegamos apenas as 4 primeiras colunas
                funcoes_membro_str = ', '.join(funcoes_membro.split(','))  # Converte a lista de funções em uma string
                print(f"{nome:<20} {data_entrada:<15} {funcoes_membro_str:<30} {ativo:<10}")
                funcoes.extend(funcoes_membro.split(','))   
            # Pergunta ao usuário se deseja plotar o gráfico
            plotar = input("\nDeseja visualizar o gráfico de distribuição de funções? (s/n): ").strip().lower()
            if plotar == 's':
                plotar_grafico_funcoes(funcoes)
            else:
                print("Gráfico não será exibido.")
    except FileNotFoundError:
        print("Arquivo de membros não encontrado.")

def remover_membro():
    nome_remover = input("Nome do membro a remover: ")
    nome_remover = nome_remover.strip().title()
    membros = []
    
    with open(CAMINHO_MEMBROS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        membros = list(reader)
    
    with open(CAMINHO_MEMBROS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for linha in membros:
            if linha[0] != nome_remover:
                writer.writerow(linha)
    print("Membro removido (ou já não existia).")

def carregar_membros():
    # Caminho para o arquivo geral de membros
    caminho_membros = "./dados/membros.csv"
    
    if not os.path.exists(caminho_membros):
        print("⚠️ Arquivo de membros não encontrado.")
        return None
    
    # Carrega o arquivo de membros
    with open(caminho_membros, 'r', newline='', encoding='utf-8') as f:
        membros = list(csv.reader(f))
    
    return membros
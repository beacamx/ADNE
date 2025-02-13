import matplotlib.pyplot as plt
from collections import Counter
import csv

def gerar_estatisticas_gerais():
    total_presencas = sum(1 for _ in open('presencas.csv', 'r', encoding='utf-8')) - 1
    total_faltas = sum(1 for _ in open('faltas.csv', 'r', encoding='utf-8')) - 1
    total_cancelados = sum(1 for _ in open('cultosCancelados.csv', 'r', encoding='utf-8')) - 1
    total_cultos = total_presencas + total_faltas + total_cancelados
    
    if total_cultos > 0:
        percentual_presenca = (total_presencas / total_cultos) * 100
    else:
        percentual_presenca = 0
    
    print("\nEstatísticas Gerais:")
    print(f"Total de cultos realizados: {total_cultos - total_cancelados}")
    print(f"Total de cultos cancelados: {total_cancelados}")
    print(f"Total de presenças registradas: {total_presencas}")
    print(f"Total de faltas registradas: {total_faltas}")
    print(f"Percentual médio de presença: {percentual_presenca:.2f}%")
    
    categorias = ['Presenças', 'Faltas', 'Cultos Cancelados']
    valores = [total_presencas, total_faltas, total_cancelados]
    colors = ['green', 'red', 'gray']
    
    plt.figure(figsize=(8,6))
    plt.bar(categorias, valores, color=colors)
    plt.title("Estatísticas Gerais da Igreja")
    plt.ylabel("Quantidade")
    plt.show()    
    
def plotar_graficos_estatisticas_membros(nome, presencas, justificadas, nao_justificadas):
    # Gráfico de presenças e faltas
    labels_presenca = ['Presenças', 'Faltas']
    valores_presenca = [presencas, justificadas + nao_justificadas]
    colors_presenca = ['green', 'red']
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    if sum(valores_presenca) > 0:  # Verifica se há dados para o gráfico
        plt.pie(valores_presenca, labels=labels_presenca, autopct='%1.1f%%', startangle=90, colors=colors_presenca)
        plt.title(f"Presenças e Faltas de {nome}")
    else:
        plt.text(0.5, 0.5, 'Sem dados', ha='center', va='center', fontsize=12)
        plt.title(f"Presenças e Faltas de {nome}")
    
    # Gráfico de faltas justificadas e não justificadas
    labels_faltas = ['Justificadas', 'Não Justificadas']
    valores_faltas = [justificadas, nao_justificadas]
    colors_faltas = ['orange', 'red']
    
    plt.subplot(1, 2, 2)
    if sum(valores_faltas) > 0:  # Verifica se há dados para o gráfico
        plt.pie(valores_faltas, labels=labels_faltas, autopct='%1.1f%%', startangle=90, colors=colors_faltas)
        plt.title(f"Detalhamento de Faltas de {nome}")
    else:
        plt.text(0.5, 0.5, 'Sem dados', ha='center', va='center', fontsize=12)
        plt.title(f"Detalhamento de Faltas de {nome}")
    
    plt.tight_layout()
    plt.show()

def gerar_estatisticas_membro():
    nome_membro = input("Nome do membro: ")
    nome_membro = nome_membro.strip().title()
    total_presencas = 0
    total_faltas = 0
    justificadas = 0
    nao_justificadas = 0
    
    with open('presencas.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for linha in reader:
            if linha[1] == nome_membro:
                total_presencas += 1
    
    with open('faltas.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for linha in reader:
            if linha[1] == nome_membro:
                total_faltas += 1
                if linha[3].strip():
                    justificadas += 1
                else:
                    nao_justificadas += 1
    
    total_cultos = total_presencas + total_faltas
    percentual_presenca = (total_presencas / total_cultos * 100) if total_cultos > 0 else 0
    
    print(f"\nEstatísticas de {nome_membro}:")
    print(f"Total de cultos: {total_cultos}")
    print(f"Total de presenças: {total_presencas}")
    print(f"Total de faltas: {total_faltas} (Justificadas: {justificadas}, Não Justificadas: {nao_justificadas})")
    print(f"Percentual de presença: {percentual_presenca:.2f}%")
    
    # Verifica se há dados válidos para plotar os gráficos
    if total_cultos > 0:
        plotar_graficos_estatisticas_membros(nome_membro, total_presencas, justificadas, nao_justificadas)
    else:
        print("Nenhum dado disponível para gerar gráficos.")
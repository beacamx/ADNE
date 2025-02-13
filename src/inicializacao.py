import os
import csv
import argparse
from utils import mes_nome

def criar_pastas_do_ano(ano):
    """
    Cria pastas para todos os meses de um ano específico.
    
    :param ano: Ano para o qual as pastas serão criadas.
    """
    # Itera sobre todos os meses (1 a 12)
    for mes in range(1, 13):
        # Define o caminho para a pasta do mês
        caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
        
        # Cria a pasta do mês, se não existir
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
            print(f"Pasta criada: {caminho_pasta}")
        else:
            print(f"Pasta já existe: {caminho_pasta}")

def inicializar_arquivos(ano):
    """
    Cria as pastas dos meses e os arquivos necessários (presencas.csv, faltas.csv, cultos_cancelados.csv)
    para um ano específico.
    
    :param ano: Ano para o qual as pastas e arquivos serão criados.
    """
    # Cria as pastas dos meses
    criar_pastas_do_ano(ano)
    
    # Lista de arquivos a serem criados (exceto membros.csv)
    arquivos = {
        'presencas.csv': ['Data', 'Nome', 'Função', 'Observação'],
        'faltas.csv': ['Data', 'Nome', 'Função que iria desempenhar', 'Justificativa'],
        'cultos_cancelados.csv': ['Data', 'Motivo']
    }
    
    # Itera sobre todos os meses (1 a 12)
    for mes in range(1, 13):
        # Define o caminho para a pasta do mês
        caminho_pasta = f"dados/{ano}/{mes:02d}_{mes_nome(mes)}"
        
        # Cria os arquivos CSV dentro da pasta do mês
        for arquivo, colunas in arquivos.items():
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            if not os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(colunas)
                print(f"Arquivo {arquivo} criado em {caminho_pasta}.")
            else:
                print(f"Arquivo {arquivo} já existe em {caminho_pasta}.")
                
if __name__ == "__main__":
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Inicializa pastas e arquivos para um ano específico.")
    parser.add_argument("ano", type=int, help="Ano para o qual as pastas e arquivos serão criados.")
    
    # Obtém o ano passado como argumento
    args = parser.parse_args()
    
    # Chama a função para inicializar os arquivos
    inicializar_arquivos(args.ano)
import csv
import os
from enum import Enum
from flask import Flask

app = Flask(__name__)

from inicializacao import inicializar_arquivos
from utils import mes_nome
from membros import adicionar_membro, atualizar_membro, remover_membro, visualizar_membros
from estatisticas import gerar_estatisticas_gerais, gerar_estatisticas_membro
from registros import registrar_presenca, registrar_falta, registrar_culto_cancelado

class OpcoesMenu(Enum):
    BANCO_MEMBROS = '1'
    ESTATISTICAS_GERAIS = '2'
    ESTATISTICAS_MEMBRO = '3'
    REGISTRO_ESCALA = '4'
    SAIR = '5'

class OpcoesBancoMembros(Enum):
    ADICIONAR = '1'
    ALTERAR = '2'
    REMOVER = '3'
    VISUALIZAR = '4'

class OpcoesRegistroEscala(Enum):
    REGISTRAR_CULTO = '1'
    REGISTRAR_CULTO_CANCELADO = '2'
    
class OpcoesRegistrarCulto(Enum):
    PRESENCA = '1'
    FALTA = '2'
    
def exibir_menu(titulo, opcoes):
    """
    Exibe um menu com opções e retorna a escolha do usuário.
    """
    print(f"\n{titulo}:")
    for chave, valor in opcoes.items():
        print(f"{chave}. {valor}")
    return input("Escolha uma opção: ")

def menu_banco_membros():
    """
    Exibe o menu do banco de membros e gerencia as opções.
    """
    opcoes = {e.value: e.name.replace('_', ' ').title() for e in OpcoesBancoMembros}
    escolha = exibir_menu("Banco de Membros", opcoes)
    
    if escolha == OpcoesBancoMembros.ADICIONAR.value:
        adicionar_membro()
    elif escolha == OpcoesBancoMembros.ALTERAR.value:
        atualizar_membro()
    elif escolha == OpcoesBancoMembros.REMOVER.value:
        remover_membro()
    elif escolha == OpcoesBancoMembros.VISUALIZAR.value:
        visualizar_membros()

def menu_registro_escala():
    """
    Exibe o menu de registro de escala e gerencia as opções.
    """
    opcoes = {e.value: e.name.replace('_', ' ').title() for e in OpcoesRegistroEscala}
    escolha = exibir_menu("Registro de Escala", opcoes)
    
    if escolha == OpcoesRegistroEscala.REGISTRAR_CULTO.value:
        sub_opcoes = {e.value: e.name.replace('_', ' ').title() for e in OpcoesRegistrarCulto}
        sub_escolha = exibir_menu("Registrar Culto", sub_opcoes)
        
        if sub_escolha == OpcoesRegistrarCulto.PRESENCA.value:
            registrar_presenca()
        elif sub_escolha == OpcoesRegistrarCulto.FALTA.value:
            registrar_falta()
    elif escolha == OpcoesRegistroEscala.REGISTRAR_CULTO_CANCELADO.value:
        registrar_culto_cancelado()

def menu():
    """
    Exibe o menu principal e gerencia as opções escolhidas pelo usuário.
    """
    while True:
        opcoes = {e.value: e.name.replace('_', ' ').title() for e in OpcoesMenu}
        opcao = exibir_menu("Menu Principal", opcoes)
        
        if opcao == OpcoesMenu.BANCO_MEMBROS.value:
            menu_banco_membros()
        elif opcao == OpcoesMenu.ESTATISTICAS_GERAIS.value:
            gerar_estatisticas_gerais()
        elif opcao == OpcoesMenu.ESTATISTICAS_MEMBRO.value:
            gerar_estatisticas_membro()
        elif opcao == OpcoesMenu.REGISTRO_ESCALA.value:
            menu_registro_escala()
        elif opcao == OpcoesMenu.SAIR.value:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

app.run()
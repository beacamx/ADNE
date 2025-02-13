PYTHON = python
SRC_DIR = src
DATA_DIR = dados

# Comando padrão (executa o programa)
run:
	@echo "Executando o programa..."
	@$(PYTHON) $(SRC_DIR)/main.py

# Inicializa as pastas e arquivos para um ano específico
init:
	@echo "Inicializando pastas e arquivos..."
	@$(PYTHON) $(SRC_DIR)/inicializacao.py $(ANO)

# Limpa arquivos temporários e pastas de dados (cuidado!)
clean:
	@echo "Limpando arquivos temporários..."
	@rm -rf $(DATA_DIR)/*
	@echo "Pastas de dados limpas."

# Instala dependências (se houver)
install:
	@echo "Instalando dependências..."
	@pip install -r requirements.txt

# Executa testes (se houver)
test:
	@echo "Executando testes..."
	@$(PYTHON) -m pytest tests/

# Ajuda (lista os comandos disponíveis)
help:
	@echo "Comandos disponíveis:"
	@echo "  make run       - Executa o programa."
	@echo "  make init ANO=<ano> - Inicializa pastas e arquivos para o ano especificado."
	@echo "  make clean     - Limpa arquivos temporários e pastas de dados."
	@echo "  make install   - Instala dependências."
	@echo "  make test      - Executa testes."
	@echo "  make help      - Exibe esta mensagem de ajuda."
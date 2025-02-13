## Inicialização do Projeto

Para configurar e inicializar as pastas e arquivos necessários para um ano específico, siga os passos abaixo:

### Pré-requisitos

1. **Python 3**: Certifique-se de que o Python 3 está instalado no seu sistema.
   - Verifique a instalação com o comando:
    ```bash
    python3 --version
    ```
   - Caso não tenha o Python instalado, siga as instruções em [python.org](https://www.python.org/).

2. **Make**: Certifique-se de que o `make` está instalado no seu sistema.
   - Verifique a instalação com o comando:
    ```bash
    make --version
    ```
   - Caso não tenha o `make` instalado, siga as instruções para o seu sistema operacional:
     - **Linux**: Instale via gerenciador de pacotes (ex: `sudo apt install make`).
     - **macOS**: Já vem pré-instalado.
     - **Windows**: Instale o [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) ou use o WSL (Windows Subsystem for Linux).

### Passos para Inicialização

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
2. **Instale as dependências (se houver)**:
```bash
make install
```
3. **Inicialize as Pastas e Arquivos**:
Para inicializar as pastas e arquivos necessários para um ano específico, use o comando make init passando o ano como argumento. Por exemplo, para o ano 2024:
```bash
python src/inicializacao.py 2024
```
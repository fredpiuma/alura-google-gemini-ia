# Arquivo main.py

# Este é o ponto de entrada do aplicativo Python.
# Aqui você pode escrever o código principal do seu projeto.

import os

def main():
    print("Olá, mundo!")
    print(__name__)
    print("Informações do arquivo:")
    print("Caminho absoluto do arquivo:", os.path.abspath(__file__))
    print("Nome do arquivo:", os.path.basename(__file__))
    print("Diretório do arquivo:", os.path.dirname(os.path.abspath(__file__)))
    print("Informações do projeto:")
    print("Diretório do projeto:", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    main()
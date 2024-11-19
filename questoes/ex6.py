import csv
import os

def ler_dados_delimitados(arquivo_txt):
    """
    Lê um arquivo com dados delimitados por ponto e vírgula (;)
    e exibe os dados no terminal.
    """
    if not os.path.exists(arquivo_txt):
        print(f"Arquivo '{arquivo_txt}' não encontrado.")
        return

    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        leitor_csv = csv.reader(file, delimiter=';')
        
        cabecalho = next(leitor_csv, None)
        print(f"Cabeçalho: {cabecalho}")

        print("\nDados dos usuários:")
        for linha in leitor_csv:
            print(linha)

def main():
    arquivo_txt = os.path.join("data", "dados_usuarios_novos.txt")
    ler_dados_delimitados(arquivo_txt)

if __name__ == "__main__":
    main()

import pandas as pd
import os
from collections import Counter

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")

def carregar_dados():
    """
    Carrega os dados do arquivo e retorna um DataFrame.
    """
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return None

    try:
        return pd.read_csv(arquivo, delimiter=";")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

def exibir_top_5_linguagens(dados):
    """
    Exibe as 5 linguagens mais citadas entre os INFNETianos e a contagem de vezes que cada uma foi mencionada.
    """
    if dados is None:
        print("Os dados não foram carregados. O exercício será pulado.")
        return

    linguagens = []

    if 'linguagens de programação' in dados.columns:
        for hobby in dados['linguagens de programação'].dropna():
            linguagens.extend(hobby.split(", "))

    contagem = Counter(linguagens)
    top_5 = contagem.most_common(5)

    if top_5:
        print("\nAs 5 linguagens mais citadas entre os INFNETianos são:")
        for linguagem, qtd in top_5:
            print(f"{linguagem}: {qtd} vezes")
    else:
        print("\nNenhuma linguagem foi encontrada nos dados.")

dados = carregar_dados()
exibir_top_5_linguagens(dados)

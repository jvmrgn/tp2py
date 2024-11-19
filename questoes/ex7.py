import pandas as pd
import ast
import os

def carregar_dados(arquivo):
    """
    Carrega os dados de um arquivo CSV e converte colunas com listas ou tuplas.
    """
    if not os.path.exists(arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    dados = pd.read_csv(arquivo, sep=';', encoding='utf-8')

    colunas_para_converter = ['hobbies', 'linguagens de programação', 'jogos']
    for coluna in colunas_para_converter:
        dados[coluna] = dados[coluna].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])
    return dados

def salvar_dados(dataframe, pasta_saida):
    """
    Salva os dados em arquivos CSV e JSON na pasta de saída.
    """
    os.makedirs(pasta_saida, exist_ok=True)

    caminho_csv = os.path.join(pasta_saida, "INFwebNet_organizado.csv")
    caminho_json = os.path.join(pasta_saida, "INFwebNet_organizado.json")

    dataframe.to_csv(caminho_csv, index=False, encoding='utf-8')

    with open(caminho_json, 'w', encoding='utf-8') as json_file:
        dataframe.to_json(json_file, orient="records", indent=4, force_ascii=False)

def main():
    """
    Função principal: carrega, organiza e salva os dados.
    """
    pasta_dados = os.path.join("data")
    arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")
    pasta_saida = os.path.join(pasta_dados, "saida")

    try:
        dados = carregar_dados(arquivo)
        print(dados)
        salvar_dados(dados, pasta_saida)
        print(f"Dados organizados salvos em: {pasta_saida}")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()

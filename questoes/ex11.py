import pandas as pd
import os

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "INFwebNet.csv")

dados = pd.read_csv(arquivo, delimiter=",")

print(dados.columns)

pasta_grupos = os.path.join("data", "grupos")
os.makedirs(pasta_grupos, exist_ok=True)

for estado in dados['estado'].unique():
    dados_estado = dados[dados['estado'] == estado]
    
    nome_arquivo = f"grupo_{estado}.csv"
    caminho_arquivo = os.path.join(pasta_grupos, nome_arquivo)
    
    dados_estado.to_csv(caminho_arquivo, index=False, sep=";")
    
    print(f"Arquivo salvo: {caminho_arquivo}")

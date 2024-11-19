import pandas as pd
import os

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "INFwebNet.csv")

dados = pd.read_csv(arquivo, delimiter=";")

arquivo_json = os.path.join(pasta_dados, "INFwebNet_Data.json")

dados.to_json(arquivo_json, orient="records", lines=False)

print(f"Arquivo JSON salvo em: {arquivo_json}")

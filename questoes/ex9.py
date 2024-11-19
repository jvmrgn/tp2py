import os
import pandas as pd

def preencher_valores_ausentes(dataframe):
    """
    Preenche valores ausentes em colunas específicas com critérios definidos.
    """
    if 'idade' in dataframe.columns:
        media_idade = dataframe['idade'].mean()
        dataframe['idade'] = dataframe['idade'].fillna(round(media_idade))
    else:
        print("A coluna 'idade' não foi encontrada no dataset.")
    
    if 'hobbies' in dataframe.columns:
        dataframe['hobbies'] = dataframe['hobbies'].apply(lambda x: [] if pd.isnull(x) else x)
    else:
        print("A coluna 'hobbies' não foi encontrada no dataset.")
    
    return dataframe

def main():
    pasta_dados = os.path.join("data")
    arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")
    
    dados_usuarios_novos = pd.read_csv(arquivo, sep=";")
    
    print("Colunas do dataset:")
    print(dados_usuarios_novos.columns)
    print("\nAntes de preencher os valores ausentes:")
    print(dados_usuarios_novos.head())
    
    dados_usuarios_novos = preencher_valores_ausentes(dados_usuarios_novos)
    
    print("\nApós preencher os valores ausentes:")
    print(dados_usuarios_novos.head())

if __name__ == "__main__":
    main()

# O valor ausenta na idade de idade foi preenchjido pela média de idade de todoas as pessoas no DataSet. A média é uma estratégia comum para preencher valores ausentes numéricos.
# Os valores ausentes nos hobbies foram preenchidos com uma lista vazia. Optei por esta opção pois ai ele deixa a pessoa com a lista de hobbies vázia já que não temos a informação.

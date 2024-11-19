import pandas as pd
import os

def calcular_media_idade(arquivo_json):
    """
    Lê o arquivo JSON e calcula a média de idade dos INFNETianos.
    """
    try:
        if not os.path.exists(arquivo_json):
            print(f"O arquivo {arquivo_json} não foi encontrado.")
            return
        
        df = pd.read_json(arquivo_json, encoding='utf-8')

        if "idade" not in df.columns:
            print("O arquivo JSON não contém a coluna 'idade'.")
            return

        media_idade = df["idade"].mean()
        print(f"A média de idade dos INFNETianos é: {media_idade:.2f} anos.")
    except ValueError:
        print(f"Erro ao processar o arquivo {arquivo_json}. Verifique o formato.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    arquivo_json = os.path.join("data", "INFwebNET.json")
    calcular_media_idade(arquivo_json)

if __name__ == "__main__":
    main()

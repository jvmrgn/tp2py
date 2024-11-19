import csv
import json
import os

def ler_csv_para_dicionario(arquivo_csv):
    """
    Lê os dados de um arquivo CSV e retorna uma lista de dicionários.
    Faz validação para garantir que os dados sejam consistentes.
    """
    dados = []
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as file:
            leitor_csv = csv.DictReader(file)
            
            for linha in leitor_csv:
                nome = linha.get("nome", "").strip()
                idade_str = linha.get("idade", "").strip()
                cidade = linha.get("cidade", "").strip()
                estado = linha.get("estado", "").strip()

                if not nome or not cidade or not estado:
                    print(f"Erro: Linha inválida encontrada e será ignorada: {linha}")
                    continue

                try:
                    idade = int(idade_str)
                    if idade <= 0:
                        raise ValueError
                except ValueError:
                    print(f"Erro: Idade inválida para o usuário '{nome}', linha ignorada.")
                    continue

                dados.append({
                    "nome": nome,
                    "idade": idade,
                    "cidade": cidade,
                    "estado": estado
                })

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_csv} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    return dados

def exportar_para_json(dados, arquivo_json):
    """
    Exporta uma lista de dicionários para um arquivo JSON.
    """
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)
        print(f"Dados exportados com sucesso para o arquivo {arquivo_json}.")
    except Exception as e:
        print(f"Erro ao exportar para JSON: {e}")

def main():
    arquivo_csv = os.path.join("data", "INFwebNet.csv")
    arquivo_json = os.path.join("data", "INFwebNET.json")

    dados = ler_csv_para_dicionario(arquivo_csv)

    if not dados:
        print("Nenhum dado válido encontrado. O arquivo JSON não será gerado.")
        return

    exportar_para_json(dados, arquivo_json)

if __name__ == "__main__":
    main()

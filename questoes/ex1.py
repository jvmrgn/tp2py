import csv
import os

def ler_dados_txt(arquivo_txt):
    """
    Lê o arquivo texto com dados dos usuários e retorna uma lista de dicionários contendo as informações.
    Faz o tratamento de dados inválidos.
    """
    usuarios = []

    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        for linha in file:
            partes = linha.strip().split('?')

            if len(partes) < 4: 
                print(f"Erro: Linha inválida encontrada e será ignorada: {linha.strip()}")
                continue

            nome = partes[0].strip()
            idade_str = partes[1].strip()
            cidade = partes[2].strip()
            estado = partes[3].strip()

            if not nome or not cidade or not estado:
                print(f"Erro: Dados incompletos encontrados e serão ignorados: {linha.strip()}")
                continue

            try:
                idade = int(idade_str) 
                if idade <= 0:
                    raise ValueError
            except ValueError:
                print(f"Erro: Idade inválida para o usuário '{nome}', linha ignorada.")
                continue

            usuarios.append({
                "nome": nome,
                "idade": idade,
                "cidade": cidade,
                "estado": estado
            })

    return usuarios

def exportar_para_csv(dados, arquivo_csv):
    """
    Exporta os dados fornecidos para um arquivo CSV.
    """
    campos = ["nome", "idade", "cidade", "estado"]

    with open(arquivo_csv, 'w', encoding='utf-8', newline='') as file:
        escritor_csv = csv.DictWriter(file, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(dados)

    print(f"Dados exportados com sucesso para o arquivo {arquivo_csv}.")

def main():
    arquivo_txt = os.path.join("data", "rede_INFNET_atualizado.txt")
    arquivo_csv = os.path.join("data", "INFwebNet.csv")

    dados_usuarios = ler_dados_txt(arquivo_txt)

    if not dados_usuarios:
        print("Nenhum dado válido foi encontrado. O arquivo CSV não será gerado.")
        return

    exportar_para_csv(dados_usuarios, arquivo_csv)

if __name__ == "__main__":
    main()

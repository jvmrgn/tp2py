import pandas as pd
import os

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")

dados = pd.read_csv(arquivo, delimiter=";")

def filtrar_por_ano_nascimento(ano_inicio, ano_fim):
    """
    Filtra os usuários que nasceram entre os anos especificados.
    """
    dados['data de nascimento'] = pd.to_datetime(dados['data de nascimento'], errors='coerce')

    dados['ano_nascimento'] = dados['data de nascimento'].dt.year

    usuarios_filtrados = dados[(dados['ano_nascimento'] >= ano_inicio) & (dados['ano_nascimento'] <= ano_fim)]

    return usuarios_filtrados

try:
    ano_inicio_input = input("Digite o ano de início do intervalo (ou pressione Enter para pular): ")
    ano_fim_input = input("Digite o ano final do intervalo (ou pressione Enter para pular): ")
    
    if ano_inicio_input == "" or ano_fim_input == "":
        print("Você escolheu pular a pergunta sobre intervalo de anos.")
    else:
        ano_inicio = int(ano_inicio_input)
        ano_fim = int(ano_fim_input)
        
        if ano_inicio > ano_fim:
            print("O ano de início não pode ser maior que o ano final.")
        else:
            usuarios = filtrar_por_ano_nascimento(ano_inicio, ano_fim)
            print(f"\nUsuários que nasceram entre {ano_inicio} e {ano_fim}:")
            print(usuarios)
except ValueError:
    print("Por favor, insira um valor válido para os anos.")

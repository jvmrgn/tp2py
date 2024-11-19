import pandas as pd
import os

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")

dados = pd.read_csv(arquivo, delimiter=";")

def buscar_e_selecionar_usuario(nome_busca):
    """
    Busca os INFNETianos pelo nome e exibe uma lista para o usuário selecionar um deles.
    """
    usuarios_encontrados = dados[dados['nome'].str.contains(nome_busca, case=False, na=False)]
    
    if usuarios_encontrados.empty:
        print("Nenhum usuário encontrado com esse nome.")
        return None

    print(f"\nUsuários encontrados com o nome '{nome_busca}':")
    for idx, row in usuarios_encontrados.iterrows():
        print(f"{idx}: {row['nome']} {row['sobrenome']} - {row['cidade']}, {row['estado']}")
    
    try:
        escolha = int(input(f"\nDigite o número do INFNETiano que deseja selecionar (0 a {len(usuarios_encontrados) - 1}): "))
        if 0 <= escolha < len(usuarios_encontrados):
            usuario_selecionado = usuarios_encontrados.iloc[escolha]
            print("\nINFNETiano selecionado:")
            print(usuario_selecionado)
            return usuario_selecionado
        else:
            print("Escolha inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None

nome_busca = input("Digite o nome do INFNETiano que deseja buscar: ")
buscar_e_selecionar_usuario(nome_busca)

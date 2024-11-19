import pandas as pd
import os

pasta_dados = os.path.join("data")
arquivo = os.path.join(pasta_dados, "dados_usuarios_novos.txt")

dados = pd.read_csv(arquivo, delimiter=";")

def buscar_e_selecionar_usuario(nome_busca):
    """
    Busca os INFNETianos pelo nome e exibe uma lista para o usuário selecionar um deles.
    Permite que o usuário pule digitando 'pular'.
    """
    if nome_busca.lower() == "pular":
        print("Busca de usuário pulada.")
        return None

    usuarios_encontrados = dados[dados['nome'].str.contains(nome_busca, case=False, na=False)]

    if usuarios_encontrados.empty:
        print("Nenhum usuário encontrado com esse nome.")
        return None

    print(f"\nUsuários encontrados com o nome '{nome_busca}':")
    for idx, row in usuarios_encontrados.iterrows():
        print(f"{idx}: {row['nome']} {row['sobrenome']} - {row['cidade']}, {row['estado']}")

    try:
        escolha = input(f"\nDigite o número do INFNETiano que deseja selecionar (ou 'pular' para cancelar): ")
        if escolha.lower() == "pular":
            print("Seleção de usuário pulada.")
            return None

        escolha = int(escolha)
        if 0 <= escolha < len(usuarios_encontrados):
            usuario_selecionado = usuarios_encontrados.iloc[escolha]
            print("\nINFNETiano selecionado:")
            print(usuario_selecionado)
            return usuario_selecionado
        else:
            print("Escolha inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'pular'.")
        return None

def atualizar_dados_usuario(usuario):
    """
    Permite atualizar os dados de um INFNETiano selecionado.
    Permite que o usuário pule digitando 'pular'.
    """
    if usuario is None:
        print("Nenhum usuário selecionado para atualizar.")
        return None

    print("\n--- Atualizando Dados do INFNETiano ---")

    def obter_novo_valor(campo, valor_atual):
        novo_valor = input(f"{campo} atual: {valor_atual}\nNovo {campo} (ou 'Enter' para manter, 'pular' para cancelar): ")
        if novo_valor.lower() == "pular":
            return "pular"
        return novo_valor or valor_atual

    campos = ['sobrenome', 'email', 'cidade', 'estado', 'hobbies', 'jogos']
    for campo in campos:
        novo_valor = obter_novo_valor(campo, usuario[campo])
        if novo_valor == "pular":
            print("Atualização de dados cancelada.")
            return None
        usuario[campo] = novo_valor

    print("\nDados atualizados com sucesso!")
    print(usuario)
    return usuario

def salvar_alteracoes(usuario):
    """
    Salva as alterações feitas em um usuário no arquivo original.
    """
    if usuario is None:
        return

    global dados
    dados.loc[usuario.name] = usuario

    dados.to_csv(arquivo, sep=";", index=False)
    print("\nAlterações salvas com sucesso!")

nome_busca = input("Digite o nome do INFNETiano que deseja buscar (ou 'pular' para cancelar): ")
usuario_selecionado = buscar_e_selecionar_usuario(nome_busca)

if usuario_selecionado is not None:
    usuario_atualizado = atualizar_dados_usuario(usuario_selecionado)

    if usuario_atualizado is not None:
        salvar_alteracoes(usuario_atualizado)
else:
    print("Operação concluída sem alterações.")

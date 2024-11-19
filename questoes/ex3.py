import json
import os

def carregar_dados(arquivo_json):
    """
    Carrega os dados existentes do arquivo JSON.
    """
    try:
        if not os.path.exists(arquivo_json):
            return []
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {arquivo_json} está corrompido ou vazio.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        return []

def salvar_dados(dados, arquivo_json):
    """
    Salva os dados no arquivo JSON.
    """
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def cadastrar_usuario():
    """
    Permite ao usuário inserir dados de um novo INFNETiano.
    """
    nome = input("Digite o nome: ").strip()
    while not nome:
        nome = input("O nome não pode ser vazio. Digite o nome: ").strip()

    try:
        idade = int(input("Digite a idade: ").strip())
        while idade <= 0:
            idade = int(input("A idade deve ser maior que 0. Digite novamente: ").strip())
    except ValueError:
        print("Idade inválida. O cadastro será cancelado.")
        return None

    cidade = input("Digite a cidade: ").strip()
    while not cidade:
        cidade = input("A cidade não pode ser vazia. Digite novamente: ").strip()

    estado = input("Digite o estado (UF): ").strip().upper()
    while not estado or len(estado) != 2:
        estado = input("O estado deve ter 2 letras (ex: RJ). Digite novamente: ").strip().upper()

    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado
    }

def main():
    arquivo_json = os.path.join("data", "INFwebNET.json")

    print("Bem-vindo ao cadastro de novos INFNETianos!")
    pular = input("Deseja pular este exercício? (s/n): ").strip().lower()
    if pular == 's':
        print("Você optou por pular o exercício. Saindo do programa...")
        return

    dados_existentes = carregar_dados(arquivo_json)

    print("Cadastro de novos INFNETianos")
    while True:
        novo_usuario = cadastrar_usuario()
        if novo_usuario:
            dados_existentes.append(novo_usuario)
        
        continuar = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()
        if continuar != 's':
            break

    salvar_dados(dados_existentes, arquivo_json)

if __name__ == "__main__":
    main()


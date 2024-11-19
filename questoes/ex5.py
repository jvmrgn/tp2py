import json
import os

def carregar_dados(arquivo_json):
    """
    Carrega os dados existentes no arquivo JSON.
    """
    if not os.path.exists(arquivo_json):
        return []
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        return json.load(file)

def salvar_dados(arquivo_json, dados):
    """
    Salva os dados no arquivo JSON.
    """
    with open(arquivo_json, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

def inserir_infnetiano(arquivo_json):
    """
    Insere um novo INFNETiano com dados ampliados.
    """
    dados = carregar_dados(arquivo_json)

    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()

    hobbys = input("Hobbys (separados por vírgula): ").split(',')
    hobbys = [hobby.strip() for hobby in hobbys if hobby.strip()]

    coding = input("Linguagens de programação (separadas por vírgula): ").split(',')
    coding = [linguagem.strip() for linguagem in coding if linguagem.strip()]

    jogos = []
    while True:
        adicionar_jogo = input("Deseja adicionar um jogo? (s/n): ").lower()
        if adicionar_jogo != 's':
            break
        jogo = input("Jogo: ").strip()
        plataforma = input("Plataforma: ").strip()
        jogos.append({"jogo": jogo, "plataforma": plataforma})

    novo_infnetiano = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado,
        "hobbys": hobbys,
        "coding": coding,
        "jogos": jogos
    }

    dados.append(novo_infnetiano)
    salvar_dados(arquivo_json, dados)
    print(f"{nome} foi adicionado(a) com sucesso!")

def main():
    arquivo_json = os.path.join("data", "INFwebNET.json")

    print("Bem-vindo ao sistema de cadastro ampliado da INFwebNET!")
    pular = input("Deseja pular este exercício? (s/n): ").strip().lower()
    if pular == 's':
        print("Você optou por pular o exercício. Saindo do programa...")
        return

    inserir_infnetiano(arquivo_json)

if __name__ == "__main__":
    main()

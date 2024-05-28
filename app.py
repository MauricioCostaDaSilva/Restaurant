
import os

restaurantes = [{"nome":"Praça","categoria": "japones", "ativo":False},{"nome":"Pizza suprema","categoria": "Pizza", "ativo":True},{"nome":"Cantina","categoria": "Italiano", "ativo":False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print(" 1. Cadastrar restaurante")
    print(" 2. Listar restaurante")
    print(" 3. Alternar estado do restaurante")
    print(" 4. Sair \n")

def finaizar_app():
    exibir_subtitulo("Finalizar app")
def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao Menu: ")
    main()

def opcao_invalida():
    """Reetorno mensagem e retorna ao menu"""
    print("Opção invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Função responsavél por limpar o terminal e apretar texto selecionado com duas linhas de asteristico em baixo e cima"""
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """Essa função é responsavél por cadastrar um novo restaurante"""
    exibir_subtitulo("Restaurante cadastrado")
    nome_do_resutaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do {nome_do_resutaurante}: ")
    dados_do_restaurante = {"nome": nome_do_resutaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_resutaurante} foi cadastrado com sucesso! \n ")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Exibi lista dando espaçamento para alinhar as colunas """
    exibir_subtitulo("Listar novos restaurantes")
    print(f" {'Nome do Restaurante'.ljust(19)} | {'Categoria'.ljust(19)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante ["ativo"] else "desativado"
        
        print(f"→{nome_restaurante.ljust(20)}|{categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def altenar_estado_do_restaurante():
    exibir_subtitulo("alternando estado do restaurante")
    nome_restaurante = input("Digite o restaurante que deseja altenar: ")
    restaudante_encontrado= False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaudante_encontrado = True
            restaurante["ativo"] = not restaurante ["ativo"]
            mensagem = f" O restaurante foi {nome_restaurante} foi ativado com sucesso" if restaurante ["ativo"] else f"O restaurante foi desativado com sucesso."
    if not restaudante_encontrado:
        print(" O restaurante não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:

        opcao_escolhida =int(input("Escolha uma opção:")) 

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            altenar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finaizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__== "__main__":
    main()

   

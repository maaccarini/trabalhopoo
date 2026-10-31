from modelos.servicos import listar_servicos
from modelos.pet import cadastrar_pet

def menu_index() -> None :
    escolha_menu : str = f"""
    {'=' * 10} SISTEMA PET SHOP {'=' * 10}
    1 - Cadastrar Pet
    2 - Cadastrar Tutor
    3 - Listar Serviços
    4 - Buscar Pet
    5 - Novo Agendamento
    6 - Finalizar Pedido
    7 - Relatório Faturamento
    0 - Sair
    """
    menu : int = None
    while menu != 0:
        print(escolha_menu)
        menu = int(input("Digite o que deseja fazer: "))
        match menu:
            case 1 :
                cadastrar_pet()
                input("Pressione enter para continuar...")
                continue
            case 2 :
                pass
            case 3:
                # Mostra os serviços disponíveis no pet shop com seus respectivos preços.
                listar_servicos()
                input("Pressione enter para continuar...")
                continue
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 0:
                exit
            case _:
                print("Favor, inserir um dos números correspondentes!")
                continue

#Objetivo: Desenvolver um aplicativo que gerencie uma lista de compras que permita adicionar,
# remover ou listar os produtos adicionados nela.

"""1-Menu de Opções: O sistema deve fornecer um menu de opções para o usuário interagir.
As opções devem ser as seguintes:
Adicionar produto
Remover produto
Pesquisar produtos
Sair do programa"""

"""2-Adicionar Produto: O usuário deve poder adicionar um novo produto à lista de compras.
O sistema deve solicitar informações sobre o nome, unidade de medida, quantidade e descrição do produto.
As opções de unidade devem ser:
Quilograma
Grama
Litro
Mililitro
Unidade
Metro
Centímetro
Essas opções devem aparecer quando o sistema perguntar a unidade de medida."""

"""3-Controle de ID Automático: O sistema deve atribuir automaticamente um ID único para cada produto adicionado à 
lista.
4-Remover Produto: O usuário deve poder remover um produto da lista com base ID do produto. 
O sistema deve solicitar o ID do produto que o usuário deseja remover.
5-Pesquisar Produtos por Nome: O usuário deve poder pesquisar produtos na lista com base no nome ou parte do nome. 
O sistema deve exibir os resultados correspondentes e fornecer a contagem total de produtos encontrados.
6-Listar Todos os Produtos: O sistema deve ser capaz de exibir todos os produtos presentes na lista de compras, 
se houver. Contudo, o menu não deve mostrar uma opção de “Listar produtos”. A exibição deverá ocorrer toda vez 
que o menu principal for executado, acima dele.
7-Cabeçalho do Aplicativo: Deve ser exibido um cabeçalho ao iniciar o aplicativo para fornecer uma saudação e 
indicar que é uma Lista de Compras Simples.
8-Feedback de Ação: Após a execução de uma ação (como adicionar ou remover um produto), o sistema deve fornecer 
feedback indicando o resultado da ação.
9-Tratamento de Entradas Inválidas: O sistema deve ser capaz de lidar com entradas inválidas do usuário e fornecer
mensagens de erro apropriadas para orientar o usuário.
10-Encerramento do Programa: O usuário deve poder encerrar o programa de forma adequada, escolhendo a opção de 
saída no menu."""

def shopping_list():
    while True:
        print("Faça sua lista de compras! Selecione a opção desejada.")
        print("1-Adicionar produto")
        print("2-Remover produto")
        print("3-Pesquisar produtos")
        print("4-Sair do programa")

        user_input = input("Digite a opção desejada: ")
        if (user_input == "4"):
            print("Encerrando o programa, obrigada por usar!")
            break
        if user_input not in ("1", "2", "3"):
            print("Opção inválida. Tente novamente.")
            continue

        if user_input == "1":
            name_prdt = input("Digite o nome do produto: ")
            number_prdt = float(input("Digite a quantidade do produto: "))
            unit_of_measure_prdt = input("Qual a unidade de medida do produto (g, Kg, mL, L, cm, e m): ")
            description_prdt = input("Descreva o produto: ")

            while True:
                print("Deseja adicionar mais produtos?")
                add_prdt = input("Digite [1] para SIM, e [2] para NÃO: ")
                if add_prdt not in ("1", "2"):
                    print("Opção inválida. Tente novamente.")
                    break
                if add_prdt == "1":
                    name_prdt = input("Digite o nome do produto: ")
                    number_prdt = float(input("Digite a quantidade do produto: "))
                    unit_of_measure_prdt = input("Qual a unidade de medida do produto (g, Kg, mL, L, cm, e m): ")
                    description_prdt = input("Descreva o produto: ")
                else:
                    break

shopping_list()









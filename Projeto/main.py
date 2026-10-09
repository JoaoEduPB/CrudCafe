from banco import *

criar_tabela()



while True:
    print('''
    CRUD CAFETERIA

    1-Adcionar um produto
    2-Vizualizar estoque
    3-Apagar produto
    4-Sair
    ''')
    n= int(input("Digite ua opção: "))
    if n == 4:
        break
    elif n == 1:
        name = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        qtd = int(input("Digite a quantidade em estoque: "))
        inserir_dados(name, valor, qtd)
        print("Entrada Adcionada!")
    elif n == 2:
        vizualizar()
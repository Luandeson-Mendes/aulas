pessoas = []
for x in range(10):
    nome = input("Digite um nome: ")
    pessoas.append(nome)
opcao = -1
while (opcao != 0):
    print("1 - Pesquisar uma pessoa")
    print("2 - Ver quantidade pessoas cadastradas")
    print("0 - Encerrar programa")
    opcao = int(input("Digite a opção escolhida: "))
    if(opcao == 1):
        nome = input("Digite o nome pra pesquisa")
        if(nome in pessoas):
            print (f"{nome} está na lista")
        else:
            print("Não está na lista")
    elif (opcao == 2):
        print(len(pessoas))
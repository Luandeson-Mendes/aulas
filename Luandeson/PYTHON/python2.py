nome = str("Escreva os nomes das pessoas")
ma = 0
while (nome != "FIM" and nome != "fim"):
    nome = str(input("Digite um nome: "))
    if (nome == "maria" or nome == "Maria" or nome == "MARIA"):
        print(ma)
        ma += 1
print (ma)
bolo = int(input("Digite um número: "))
de_molhangou = 0
meu_favorito = bolo
while (bolo!=0):
    bolo = int(input("Digite um número: "))
    meu_favorito +=bolo
    de_molhangou +=1
print (meu_favorito/de_molhangou)
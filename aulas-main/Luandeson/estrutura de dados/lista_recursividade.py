class Elemento:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

e1 = Elemento(91, None)
e2 = Elemento(92, None)
e3 = Elemento(93, None)
e4 = Elemento(94, None)

e1.proximo = e2
e2.proximo = e3
e3.proximo = e4
primeiro = e1

'''print(e1)
print(e1.valor)
#    {ELEMENTO 1}.valor
print(e1.proximo)
print(e1.proximo.valor)
#    {ELEMENTO 2}.valor
print(e1.proximo.proximo)
print(e1.proximo.proximo.valor)
#    {ELEMENTO 3}.valor
print(e1.proximo.proximo.proximo)
print(e1.proximo.proximo.proximo.valor)
#    {ELEMENTO 4}.valor'''
'''táquion '''

#while (primeiro != None):
#    print(primeiro)
#    print(primeiro.valor)
#    primeiro = primeiro.proximo


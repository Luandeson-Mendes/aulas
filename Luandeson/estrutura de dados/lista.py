from lista_recursividade import Elemento
class lista:
    def __init__ (self, primeiro):
        self.primeiro = primeiro
    
    def print_lista(self):
        aux = self.primeiro
        if (aux != None):
            while (aux.proximo != None):
                print (aux.valor)
                aux = aux.proximo
        else:
            print ("Lista Vazia")
        return aux

#    def AdicionarElementoInicio (self):
#        minha_lista
        
        
    def AdicionarElementoFinal (self, numero):
            aux = self.primeiro
            if (aux != None):
                while (aux.proximo != None):
                    aux = aux.proximo
                e = Elemento(numero, None)
                aux.proximo = e
            else:
                #Criar novo elemento
                e = Elemento(numero, None)
                self.primeiro = e
                Elemento = Elemento
            



'''    def  RemoverElementoInicio (self):
        
        
    def  RemoverEl        return auxementoFinal (self):
    def  Elemento (self):
    def  Elemento (self):Element
    
minha_lista = Lista()
minha_lista.AdicionarElementoFin    def print_lista(self):
        aux = self.primeiro
        if (aux != None):
        else:
            #Criar novo elemento
            Elemento = Elemento
            
            print ("Lista Vazia")
        return aux
'''

'''vetor = []
vetor.append[1]
vetor.append[2]
vetor.append[3]
print(vetor)
'''
MinhaLista = lista
MinhaLista.AdicionarElementoFinal(81)
MinhaLista.AdicionarElementoFinal(82)
MinhaLista.AdicionarElementoFinal(83)

print (MinhaLista)
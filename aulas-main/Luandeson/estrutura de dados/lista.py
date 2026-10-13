from lista_recursividade import Elemento
class lista:
    def __init__ (self, primeiro):
        self.primeiro = primeiro
    
    def ImprimeLista(self):
        aux = self.primeiro
        if (aux != None):
            while (aux.proximo != None):
                print (aux.valor)
                aux = aux.proximo
        else:
            print ("Lista Vazia")
        return aux

    def AdicionarElementoInicio (self, numero):
        aux = self.primeiro
        if(aux != None):
            e = Elemento(numero, None)
            e.proximo = self.primeiro
            self.primeiro = e
        else:
            e = Elemento(numero, None)
            self.primeiro = e
        
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
                
            



    def  RemoverElementoInicio (self):
        aux = self.primeiro
        if(aux!= None):
            self.primeiro = self.primeiro.proximo
            del(aux)
        else:
            print("\nA lista está vazia!")
        
        
    def  RemoverElementoFinal (self):
        aux = self.primeiro
        if (aux != None):
            if (aux.proximo == None):
                del(self.primeiro)
                self.primeiro = None
            else:
                while (aux.proximo.proximo != None):
                    aux = aux.proximo
                del(aux.proximo)
                aux.proximo = None
        else:
            print("\nA lista está vazia!")
        


#   RemoverQualquerElemento


MinhaLista = lista
MinhaLista.AdicionarElementoFinal(91)
MinhaLista.AdicionarElementoFinal(92)
MinhaLista.AdicionarElementoFinal(93)

MinhaLista.RemoverElementoFinal(91)
MinhaLista.ImprimeLista()
#Recursividade

#def mdc(num, den):
#    if (den == 0):
#        return num
#    else:
#        return mdc(den, (num % den))
    
#n1 = 42
#n2 = 28
#print(mdc(n1, n2))



def mdc_interativo(numerador, denominador):
    while (denominador != 0):
        numerador, denominador = denominador, numerador % denominador
    return numerador

n1 = 42
n2 = 28
print(mdc_interativo(n1, n2))
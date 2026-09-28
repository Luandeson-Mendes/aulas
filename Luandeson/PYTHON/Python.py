
n = int(input("Digite um número: "))
num = [1, 2, 3, ]
if n in num:
    print("Está na lista")
else: 
    print("Não está na lista")
    
    
for i in range(len(num)):
    num[i] = num[i] %2
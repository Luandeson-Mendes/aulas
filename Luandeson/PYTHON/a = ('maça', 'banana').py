nome = []
nota = []
nota2 = []
for x in range(5):
    nome.append(input("Digite seu nome: "))
    nota.append(int(input("Digite sua primeira nota: ")))
    nota2.append(int(input("Digite sua segunda nota: ")))
for i in range(5):
    print(f"{nome[x]} - {nota[x]} - {nota2[x]} - {(nota[x]+nota2[x])/2}")
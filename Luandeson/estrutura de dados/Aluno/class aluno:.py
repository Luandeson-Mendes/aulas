class aluno:
    def __init__(self, nome, mat, curso, idade):
        self.nome = nome
        self.mat = mat
        self.curso = curso
        self.idade = idade
    def ImprimeDadosAlunos(self, nome, mat, curso, idade):
        print ("Dados do aluno: ")
        print
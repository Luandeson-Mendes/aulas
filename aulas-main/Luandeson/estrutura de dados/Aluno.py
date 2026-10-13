from Curso import curso
class aluno:
    def __init__(self, nome, mat, curso, idade):
        self.nome = nome
        self.mat = mat
        self.curso = curso
        self.idade = idade
    def ImprimeDadosAlunos(self, nome, mat, curso, idade):
        print ("Dados do aluno: ")
        print ("Nome: ", self.nome)
        print ("Matricula: ", self.mat)
        print ("Curso: ", self.curso)
        print ("Idade: ", self.idade)
CursoTsi = curso("TSI", "tarde", "Estrutura de Dados")
a1 = aluno("Thiago", "19362", CursoTsi, 36)
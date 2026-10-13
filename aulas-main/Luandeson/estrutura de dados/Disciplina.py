class disciplina:
    def __init__(self, nome, cargahoraria, docente, codigo):
        self.nome = nome
        self.cargahoraria = cargahoraria
        self.docente = docente
        self.codigo = codigo
        
    def ImprimeDadosDisciplina(self):
        print("DADOS DA DISCIPLINA: ")
        print("Nome:", self.nome)
        print("Carga Horaria: ", self.cargahoraria)
        print("Docente: ", self.docente)
        print("Código: ", self.codigo)
        
d1 = disciplina("Estrutura de Dados", "72 horas", "Lucas", 000)
d2 = disciplina("Python", "64 horas", "Thiago", 60)

d1.ImprimeDadosDisciplina()
d2.ImprimeDadosDisciplina()
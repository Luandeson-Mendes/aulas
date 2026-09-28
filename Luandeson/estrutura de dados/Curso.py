class curso:
    def __init__(self, nome, periodo, disciplina):
        self.nome = nome
        self.periodo = periodo
        self.disciplina = disciplina
        
    def imprimeDadosCurso(self, nome, periodo, disciplina):
        print("Nome: ", self.nome)
        print("Periodo: ", self.periodo)
        print("Disciplina: ", self.disciplina)
c1 = curso("TSI", 4, "Matemática")
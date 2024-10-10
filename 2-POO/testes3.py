class Faculdade:
    @staticmethod
    def materias(materia):
        if materia == 'Python':
            semestre = ['Analise de dados', 'Django', 'Flask API']
        elif materia == 'Banco de dados':
            semestre = ['SQL Server', 'MySQL', 'Oracle']
        else:
            semestre = 'Grade a definir'
        return semestre
    
print(Faculdade.materias('Python'))
print(Faculdade.materias('Java'))

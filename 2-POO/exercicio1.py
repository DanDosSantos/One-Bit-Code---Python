class Movie():
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.inludedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
    
    def techinal_sheet(self):   # Exibir
        print('--------Dados do Filme--------')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Está no plano? {self.inludedPlan}')
        print(f'Avaliação do filme: {self.totalEvaluation}') # inf avaliação total
        print(f'Duração do filme: {self.durationMinutes}')
        print(f'Total avaliadores: {self.evaluators}') # Informar qts avaliadores
    
    def evaluete(self, note):
        self.totalEvaluation += note  # Aqui irá add cada nota a totalEvaluation
        self.evaluators += 1  # Aqui irá add cada avaliador a evaluators

    def average(self):
        print(f'Média do filme {self.name}: {self.totalEvaluation / self.evaluators:.2f}')


movie = Movie('Interestelar', 2014, True, 290)
movie.evaluete(9.2) # vai somar em TOTAL EVALUATION
movie.evaluete(10)  # vai somar em TOTAL EVALUATION
movie.evaluete(8.5) # vai somar em TOTAL EVALUATION
movie.techinal_sheet() # chamando os prints 
movie.average() # calculando a média

class Movie():
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.inludedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):       # Metodo STR construtor
        return f'Nome do filme: {self.name} \nAno de lançamento: {self.yearLaunch} \nNota: {self.note}'
    
    def techinal_sheet(self):                   # Metodo de instancias
        print('--------Dados do Filme--------')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Está no plano? {self.inludedPlan}')
        print(f'Avaliação do filme: {self.note}')
        print(f'Duração do filme: {self.durationMinutes}')

movie = Movie('Super Mario Bros', 2023, False, 8.5, 125)
movie2 = Movie('Interestelar', 2014, True, 9.2, 290)
movie.techinal_sheet()
movie2.techinal_sheet()
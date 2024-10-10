class Movie():
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.inludedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f'Nome do filme: {self.name} \nAno de lançamento: {self.yearLaunch} \nNota: {self.note}'

movie = Movie('Um amor para recordar', 2002, False, 9.1, 140)
movie2 = Movie('Interestelar', 2014, False, 9.2, 290)
print(movie.name)
print(movie.note)
print('-'*30)
print(movie2)

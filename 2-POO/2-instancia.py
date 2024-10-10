class Movie:
    name = ''
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro filme
movie = Movie()
movie.name = 'Super Mario Bros'
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 7.5
movie.durationMinutes = 130
print("---Dados do primeiro Filme---")
print(f'Nome do filme: {movie.name} \nAno de Lançamento: {movie.yearLaunch}\n')


# Segundo filme
movie2 = Movie()
movie2.name = 'Furiosa - Uma saga Mad Max'
movie2.yearLaunch = 2024
movie2.includedPlan = False
movie2.note = 8
movie2.durationMinutes = 150
print('---Dados do segundo Filme---')
print(f'Nome do filme: {movie2.name} \nAno de Lançamento: {movie2.yearLaunch} \nNota do filme: {movie2.note} \nDuração: {movie2.durationMinutes} minutos\n')


# Terceiro filme
movie3 = Movie()
movie3.name = 'Um amor para recordar'
movie3.yearLaunch = 2002
movie3.includedPlan = False
movie3.note = 9.1
movie3.durationMinutes = 140
print('---Dados do terceiro filme---')
print(f'Nome do filme: {movie3.name} \nAno de Lançamento: {movie3.yearLaunch} \nNota do filme: {movie3.note} \nDuração: {movie3.durationMinutes} minutos\n')

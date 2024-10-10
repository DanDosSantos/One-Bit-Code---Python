import glob, os, zipfile

# 1 - Diretório de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos .txt
for arquivo in glob.glob('3-Arquivos/*.txt'):
    print(arquivo)

# 3 - Listar todos os arquivos .csv
for arquivo in glob.glob('3-Arquivos/*.csv'):
    print(arquivo)

# 4 - Compactar arquivos .txt
with zipfile.ZipFile('names.zip', 'w') as zip:
    for arquivo in glob.glob('3-Arquivos/*.txt'):
        zip.write(arquivo)

# 5 - Compactar arquivos .csv
with zipfile.ZipFile('courses.zip', 'w') as zip:
    for arquivo in glob.glob('3-Arquivos/*.csv'):
        zip.write(arquivo)

# 6 - Compactar todos os arquivos
with zipfile.ZipFile('code.zip', 'w') as zip:
    for arquivo in glob.glob('3-Arquivos'):
        zip.write(arquivo)
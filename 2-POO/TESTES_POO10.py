# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro. Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True  # atributo para verificar se o livro está disponível

    def emprestimo(self):
        if self.disponivel:
            self.disponivel = False
            print('O livro foi emprestado.')
        else:
            print('O livro já está emprestado.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print('O livro foi devolvido.')
        else:
            print('O livro já está disponível.')

    def esta_disponivel(self):
        if self.disponivel:
            print('O livro está disponível!')
        else:
            print('O livro está emprestado.')

# Exemplo de uso:
livro1 = Livro('Goosebumps', 'R.L. Stine', 350)
livro1.esta_disponivel()  # Deve indicar que o livro está disponível
livro1.emprestimo()  # Deve emprestar o livro
livro1.esta_disponivel()  # Deve indicar que o livro está emprestado
livro1.devolver()  # Deve devolver o livro
livro1.esta_disponivel()  # Deve indicar que o livro está disponível novamente
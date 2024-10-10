''' Método de classe
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método estático.
'''
# Uma pessoa ira consultar informações sobre determinada matéria e verificar oq irá aprender
class Curso:
    def __init__(self, nome, trilha):
        self.nome = nome
        self.trilha = trilha

    @staticmethod
    def cursos_trilha(trilha): # A trilha irei passar como argumento lá embaixo
        if trilha == 'Python Fundamentos':
            cursos = ['Dominando o Python', 'Módulos e Pip', 'Orientação a Objetos']
        elif trilha == 'Automação com o Python':
            cursos = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual em Python']
        else:
            cursos = 'A definir'
        return cursos
    
print(Curso.cursos_trilha('Python Fundamentos'))  
print(Curso.cursos_trilha('Análise de Dados'))
print(Curso.cursos_trilha('Automação com o Python'))# <--aqui seria o argumento estatico
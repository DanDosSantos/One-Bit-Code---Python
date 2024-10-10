class Phone:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def __str__(self): # 1- Chama esse atributo automaticamente na classe
        return f'{self.marca} {self.modelo}'
    
    @staticmethod
    def fazendo_ligacao(cel_num):
        print(f"Ligando para {cel_num}") # 2- Passar o argumento la embaixo

class SmartPhone(Phone):
    def __init__(self, marca, modelo, preco, ram, memoria_interna, camera):
        super().__init__(marca, modelo, preco)
        self.ram = ram
        self.memoria_interna = memoria_interna
        self.camera = camera

motorola = Phone('Moto', 'G8', 1400)
print(motorola) # 1- Não preciso chamar um atributo dentro da classe pois o __STR__ criado dentro da classe Phone já me retorna a string
print(f'Valor do {motorola.marca} {motorola.modelo} é R${motorola.preco}')
motorola.fazendo_ligacao(11937463826) # 2- Passando o argumento
print(vars(motorola))
print('-'*60)


iphone = SmartPhone('Apple', 'Iphone 15 pro max', 7000, '6GB', '1TB', '25MP')
print(iphone)
print(f'Valor do {iphone.marca} {iphone.modelo} é R${iphone.preco} com {iphone.ram} de ram e {iphone.memoria_interna} de armazenamento')
iphone.fazendo_ligacao(2234537295)
print(vars(iphone)) # Vai me retornar tudo o que foi passado como argumento

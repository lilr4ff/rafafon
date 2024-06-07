class Carro:
    def __init__(self, marca, modelo, ano): #definir os atributos
        self.marca = marca #receber os atribusto self.exemplo = classe
        self.modelo = modelo
        self.ano =  ano
    
    def descrever(self):
        print(f"Este carro é um {self.marca}, {self.modelo},{self.ano} ")

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado")

meu_carro = Carro('Kia', 'Foda', '2021')

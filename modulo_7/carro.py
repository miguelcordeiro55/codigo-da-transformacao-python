# carro.py

class Carro:
    def _init_(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo} ({self.ano})")

    def _str_(self):
        return f"{self.marca} {self.modelo} - Ano {self.ano}"
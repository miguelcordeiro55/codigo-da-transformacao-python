# carro_eletrico.py

from carro import Carro

class CarroEletrico(Carro):
    def _init_(self, marca, modelo, ano, autonomia):
        super()._init_(marca, modelo, ano)
        self.autonomia = autonomia  # atributo exclusivo

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia: {self.autonomia} km")

    def _str_(self):
        return f"{self.marca} {self.modelo} - Ano {self.ano} - {self.autonomia} km de autonomia"
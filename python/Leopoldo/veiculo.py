# Marca, Modelo, Velocidade max., Quilometragem
# Capacidade (quantos passageiros) 
#  -> defina um valor padrão, caso não informado
class Veiculo:
    def __init__(self, marca, modelo, vel_max, kms, capacidade=5):
        self.marca = marca
        self.modelo = modelo
        self.velMax = vel_max
        self.quilometragem = kms
        self.capacidade = capacidade
    def __str__(self):
        return f'Veículo {self.marca}, modelo {self.modelo}, atinge velocidade máxima {self.velMax}km/h, comporta {self.capacidade} passageiros e já rodou {self.quilometragem} kms'

class CarroFiat(Veiculo):
    def __init__(self, modelo, vel_max, kms, capacidade=5):
        super().__init__('Fiat',modelo,vel_max,kms,capacidade)

class OnibusEscolar(Veiculo):
    def __init__(self):
        super().__init__('Mercedes','BUSAO',80,0,45)
        
v = Veiculo('Fiat', 'Uno', 100, 1500)
print(v) 
uno = CarroFiat('uno', 120, 1000, 4)
print(uno)
onibus = OnibusEscolar()
print(onibus)

#Veículo {marca}, modelo {modelo}, 
# atinge velocidade máxima {velMax}, comporta {capacidade} 
# e já rodou {quilometragem}
class Veiculo:
    def __init__(self, marca :str ='Não informada', modelo :str ='Não informado', velocidadeMax :float =0.0, km :float =0.0, capacidade :int =5) -> None:
        self.marca=marca
        self.modelo=modelo
        self.velocidadeMax=velocidadeMax
        self.km=km
        self.capacidade=capacidade
    def __str__(self) -> str:
        return 'Veículo {}, modelo {}, atinge velocidade máxima {}, comporta {} e já rodou {}'.format(self.marca, self.modelo, self.velocidadeMax, self.capacidade, self.km)

class CarroFiat(Veiculo):        
        def __init__ (self, modelo, velocidadeMax, km, capacidade=5)
             super().__init__('Fiat', modelo, velocidadeMax, km, capacidade )
             
             
if __name__=='__main__':
    v=Veiculo('bmw', '2023')
    print(v)

    

veiculos={
    'Mateus':['carro', 'moto'],
    'Pedro':['bicicleta', 'moto'],
    'Maria':['bicicleta', 'carro'],
    'José':['moto','carro'],
    'Tiago':['carro', 'bicicleta'],
}
carros=0
bicicletas=0
motos=0
for key in veiculos:
    carros=carros+veiculos[key].count('carro')
    bicicletas=bicicletas+veiculos[key].count('bicicleta')
    motos=motos+veiculos[key].count('moto')
print("Qtd de carros é :", carros)    
print("Qtd de bicicletas é :", bicicletas)    
print("Qtd de motos é :", motos) 
 
for key, value in veiculos.items():
    if 'carro' in value:
        ind=veiculos[key].index('carro')
        veiculos[key][ind]=50
    if 'moto' in value:
        ind=veiculos[key].index('moto')
        veiculos[key][ind]=25
    if 'bicicleta' in value:
        ind=veiculos[key].index('bicicleta')
        veiculos[key][ind]=10  
print(veiculos) 
for key in veiculos:
    soma= sum(veiculos[key])
    print("A soma de Mateus é %s" %(soma))            



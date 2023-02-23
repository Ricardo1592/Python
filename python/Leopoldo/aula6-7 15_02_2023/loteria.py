import random
import sys

def numeros_loteria(qtde :int, min :int, max :int):
    lista=[]
    if min>=max:
        print("Valor mínimo maior ou igual ao máximo")
        return
    if qtde > (max-min+1):  # PPara evitar um laço infinito
        qtde=max-min
    for i in range(1, qtde+1):
        num=random.randrange(min,max+1)
        while num in lista:  # Para evitar números repetidos e garantir que a qtde será a que foi informada na função
            num=random.randrange(min,max+1)
        lista=lista+[num]

    return lista
args=sys.argv
qtde=int(args[1])
min=int(args[2])
max=int(args[3])
for numero in numeros_loteria(qtde, min, max):
    print(numero)
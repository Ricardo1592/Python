numeros=[]
for i in range(1,4):
    num=int(input())
    numeros=numeros+[num]
qtd=len(numeros)
numeros.sort()
for numero in numeros:
    print(numero)



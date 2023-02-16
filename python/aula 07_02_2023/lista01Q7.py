# Soma os números impares no intervalo definido pelo usuário
numI= int(input('Digite o valor inicial do intervalo:'))
numF= int(input('Digite o valor final do intervalo:'))

somaDosImpar= 0
for i in range(numI, numF+1):
    resto = i%2
    if resto != 0:
        impar= i
        somaDosImpar= somaDosImpar + impar

print("A soma dos numeros impares é:", somaDosImpar)


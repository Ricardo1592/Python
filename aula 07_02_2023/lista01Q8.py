# Faz a conversão de Farenheit para Celsius para todos os valores do intervalo fornecido pelo usuário
numI= int(input('Digite o valor inicial do intervalo:'))
numF= int(input('Digite o valor final do intervalo:'))

somaDosImpar= 0
for i in range(numI, numF+1):
    farenheit=i
    celsius= (farenheit -32)*5/9
    print("O valor de", farenheit, "farenheit em celsius é:", celsius)



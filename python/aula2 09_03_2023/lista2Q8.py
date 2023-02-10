# # Lê uma sequência de números e para com algum negativo, depois em ordem reversa imprime os valores com dois dígitos significativos

# num=int(input("Digite o primeiro número:"))
# sequencia=[]
# while num<0:
#     int(input("número inválido, digite outro número:"))
# while num>=0:
#     sequencia=sequencia+[num]
#     num=int(input("digite outro número:"))
# print(sequencia)    
# for i in range(len(sequencia)):
#     if sequencia[i]>9 and sequencia[i]<100:
#         inverso=str(sequencia[i])
#         inverso=list(inverso)
#         inverso[0], inverso[-1]=inverso[-1], inverso[0]
#         print("".join(inverso))


# Solução do professor

n = int(input('Número negativo para:'))
numeros=[]
while n >= 0:
    if n>9 and n<100:
        numeros.append(n)
    n = int(input('numero, negativo para
    :'))

for i in range (len(numeros) -1, -1, -1):
    print(numeros[i])   

# ou

print(numeros.reverse())        





    
    


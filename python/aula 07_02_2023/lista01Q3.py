num1 = int(input("Digite o primeiro numero :"))
num2 = int(input("Digite o segundo numero :"))
num3 = int(input("Digite o terceiro numero :"))

menor=num1
if num2<menor:
    menor= num2

if num3<menor:
    menor= num3

if num3==num2 and num3==num1:
    menor= "Todos os números são iguais"

if type(menor) != str:
    print("O menor numero é:", menor)
else:    
    print(menor)
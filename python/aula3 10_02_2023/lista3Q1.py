# Programa de cadastro de curso, com seu código(inteiro positivo), nome e centro(inteiro positivo)

cursos=()
tabela=[]
codigo=1
while codigo>0:
    codigo=int(input("Digite o código do curso: "))
    if codigo >0:
        curso=input("Digite o nome do curso: ")
        centro=int(input("Digite o centro curso: "))
        while centro <0:
            centro=int(input("Número inválido digite outro: "))
        tabela=tabela+[(codigo, curso, centro)]

print(tabela)
codCentro=1
while codCentro > 0:
    codCentro= int(input('Digite número do centro:'))
    j=0
    for i in range(len(tabela)):
        if codCentro==tabela[i][2]:
            print("O centro %d é do curso %s com código %d" %(tabela[i][2], tabela[i][1], tabela[i][0]))
            j=j+1 
    if j==0:
        print("O centro não está cadastrado")    




    
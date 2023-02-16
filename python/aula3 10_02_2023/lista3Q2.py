# Programa de cadastro pessoas, com código, nome e salários sendo armazenados para cada uma

pessoas={}
codigo=1
while codigo>0:
    codigo=int(input('Digite o código de uma pessoa: '))
    if codigo>0:
        nome=input('Digite o nome dela:')
        salario=float(input('Digite o salário dela:'))
        while salario <0:
            salario=float(input('Salário inválido, digite novamente:'))
        pessoas[salario]=(nome, codigo)
 
print(pessoas)

salConsulta=float(input("Digite o salário para consulta: "))
numPessoas=0
soma=0
media=0
while salConsulta <0:
    salConsulta=float(input("Salário inválido, digite novamente: "))
for sal in pessoas:
    if sal < salConsulta:
        numPessoas=numPessoas+1
        soma=soma+sal
        print("Salário de %s é menor que R$%.2f no valor de R$%.2f, cujo código é: %d"%(pessoas[sal][0], salConsulta, sal, pessoas[sal][1]))
        

print("%d pessoas possuem salários menores que R$%.2f" %(numPessoas, salConsulta))
media= soma/numPessoas
print("A média dos salários delas e:",media)
    
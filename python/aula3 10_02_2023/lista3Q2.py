# Programa de cadastro pessoas, com código, nome e salários sendo armazenados para cada uma

pessoas={}
codigo=1
while codigo>0:
    codigo=int(input('Digite o código de uma pessoa: '))
    if codigo>0:
        nome=input('Digite o nome dela:')
        salario=float(input('Digite o salário dela:'))
        while salario <0:
            salario=float(input('Salário inválido digite novamente:'))
        pessoas[salario]=(nome, codigo)
 
print(pessoas)

salConsulta=input("Digite o salário para consulta: ")
for sal in pessoas:
    if sal < salConsulta:
        

    
pessoas=int(input())
lugar=int(input())
quartos=int(input())
valor=0
if lugar==1 and quartos==2:
    valor=600+75*pessoas 
if lugar==1 and quartos==3:
    valor=900+75*pessoas
if lugar==2 and quartos==3:
    valor=950+60*pessoas
if lugar==2 and quartos==4:
    valor=1120+60*pessoas 

valorP=valor/pessoas
print('Digite a quantidade de pessoas:')
print('Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)')
print('Digite a quantidade de quartos:')
print('Valor total da viagem: R$ %.2f'%valor)
print('Valor por pessoa: R$ %.2f'%valorP)
              
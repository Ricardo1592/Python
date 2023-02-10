num=int(input('Digite um numero:'))
while num <0:
    num=int(input('numero invalido, digite outro numero:'))
for i in range (num+1,0, -1):
    if num%i==0:
        print(i)        
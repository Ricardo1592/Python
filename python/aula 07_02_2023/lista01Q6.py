# Calcula três sequências diferentes de acordo com o número de termos definido pelo usuário

termos=int(input('Digite o número de termos:'))

# sequência a= 1 + 3/2 + 5/3 + 7/4 +...
divisorA= 1
numeradorA=1
soma=1
while divisorA<termos:
    divisao= numeradorA/divisorA
    soma = soma+divisao
    divisorA=divisorA+1
    numeradorA=numeradorA+2
    # print("dividindo {}/{}".format(numeradorA,divisorA))
print("a soma da sequência 1 + 3/2 + 5/3 + 7/4 +... com", termos, "termos é:", soma)

# sequência b= 2/500 - 5/490 + 2/480 - 5/470 +...
numeradorB=2
divisorB=500
condParadaB= divisorB - 10*termos
somaB=0
contB=1
while  divisorB > condParadaB:
    if contB%2 == 0:
        numeradorB=-5
    else:
        numeradorB=2    
    # print("dividindo {}/{}".format(numeradorB,divisorB))
    divisaoB=numeradorB/divisorB
    somaB=somaB+ divisaoB
    divisorB=divisorB - 10
    contB=contB+1
print("a soma da sequência b= 2/500 - 5/490 + 2/480 - 5/470 +... com", termos, "termos é:", somaB)
# sequência c= 37*38/1 + 36*37/2 + 35*36/3+...
divisorC=1
mult1=37
mult2=38
somaC=0
while divisorC<=termos:
    # print("calculando o valor de {}*{}/{}".format(mult1,mult2, divisorC))
    termo = mult1*mult2/divisorC
    mult1=mult1-1
    mult2=mult2-1
    divisorC=divisorC+1
    somaC=somaC+termo
print("a soma da sequência c= 37*38/1 + 36*37/2 + 35*36/3+... com", termos, "termos é:", somaC)    


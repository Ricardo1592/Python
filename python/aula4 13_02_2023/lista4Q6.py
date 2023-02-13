n=int(input("Digite o número de termos: "))
while n<0:
    n=int(input("Inválido.Digite o número de termos: "))
def serie(termo):
    if termo<2:
        t=2/500
    elif termo%2==0:
        numerador=-5
    else:
        numerador=2
        denominador= 500- (termo-1)*10  
        t=numerador/denominador

for i in range(1,n+1):
          
    print("Termo --> %d/%d ")
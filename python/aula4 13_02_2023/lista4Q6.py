n=int(input("Digite o número de termos: "))
while n<0:
    n=int(input("Inválido.Digite o número de termos: "))
def serie(termo):
    soma=0
    if termo%2==0:
        numerador=-5
    else: 
        numerador=2
    if termo==1:
        print("termo 1 --> %d/%f" %(numerador, 500-(termo-1)*10))
        soma= numerador/(500-(termo-1)*10) 
        return numerador/(500-(termo-1)*10) 
    else:
        print(termo)
        print("termo %d --> %d/%f" %(termo,numerador, 500-(termo-1)*10))
        t=numerador/(500-(termo-1)*10) 
        return t+serie(termo-1)
print(serie(n))
# for i in range(1,n+1):
          
#     print("Termo --> %d/%d ") 
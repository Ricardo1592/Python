def mdc(n1,n2):
    maior=n1
    menor=n2
    mdc=1
    if n1<n2:
        maior=n2
        menor=n1
    
    divisor=menor//2

    if maior%menor!=0:
        if maior%divisor==0 and menor%divisor==0: return divisor
        while maior%divisor!=0 or menor%divisor!=0:
            divisor=divisor-1
            mdc=divisor
    else:
        return menor       
    return mdc 

num=input()
decimais=num.split('.')[-1]  
decimais=len(decimais)
denominador=10**decimais
num=float(num)
numerador=num*10**decimais
# print(denominador)
# print(numerador)
mdc=mdc(numerador, denominador)

fraçao="{}/{}".format(int(numerador/mdc),int(denominador/mdc))
print(fraçao)
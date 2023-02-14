n=float(input())
n=int(n)
soma=0
termos=[]
def func_denominador(n :int):
    if n>=0:
        denom=(2*n+1)**0.5
        return denom
    else:
        return
def func_numerador(n):
    i=1
    numerador=1
    while i<=n:
        numerador=numerador*i
        i=i+1
    if n==0: 
        numerador=1
    elif n<0:
        return    
    return numerador
def somatorio(n):
    global soma
    global termos
    numerador=func_denominador(n)
    if n>0:
        numerador=func_numerador(n)
        denominador=func_denominador(n)
        divisao=numerador/denominador
        termos=termos+[divisao]
        soma=soma+divisao
        n=n-1
        somatorio(n)
    return soma    
soma=somatorio(n)
if len(termos)>0:termos=termos[1:]
print("S: %.12f" %(soma))
if len(termos)>0:
    for termo in termos: print("%.12f" %(termo))

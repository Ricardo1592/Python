def primos(num):
    raiz=round(num**0.5)
    if num<=1:
        return False
    for divisor in range (2, raiz+1):
        if num%divisor==0:
            return False
    return True

def pares_consecutivos(primos_lista):
    consecutivos=[]
    for i in range(1, len(primos_lista)-1):
        if i%2!=0:
            soma=primos_lista[i] + primos_lista[i+1]
            consecutivos= consecutivos + [soma/2]
    return consecutivos

def matriz(lista, t):
    lista=lista[1:10]
    print(lista)
    linhas=[0]*t
    matriz=[linhas]*t
    k=0
    for i in range(t):
        for j in range(t):
            print("i --> %d" %(i))
            print("j --> %d" %(j))
            matriz[i][j]=lista[k]
            print("k --> %d" %(k))
            k=k+1    
    return matriz

def matriz2(lista):
    matriz=[]
    for i in range(3):
        matriz.append(lista[3*i+1:3*i+4])
    return matriz


primos_lista=[]
if __name__=="__main__":
    for i in range (2,101):
        if primos(i):
            primos_lista=primos_lista+[i]
    print(primos_lista)  
    lista2=pares_consecutivos(primos_lista)
    print(lista2)
    matriz=matriz2(lista2)
    for linha in matriz:
        print(linha)
       





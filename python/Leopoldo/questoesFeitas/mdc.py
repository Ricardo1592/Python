def mdc(n1, n2):
    menor=n1
    maior=n2
    if n2<menor:
        menor=n2
        maior=n1
    if n1==n2 or maior%menor==0:
        return menor
    for i in range((menor+1)//2, 0, -1):
        if maior%i==0 and menor%i==0:
            return i
    return 1    

n1=34
n2=12
print(mdc(n1,n2))            
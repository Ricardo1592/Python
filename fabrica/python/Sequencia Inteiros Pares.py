num=int(input())
def sequencia_pares(num):
    if num>-1:
        if num%2==0:
            print(num)
        num=num-1
        sequencia_pares(num)   
    return    

if num>0: sequencia_pares(num)
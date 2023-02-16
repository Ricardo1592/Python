def palindromo(num):
    num=str(num)
    digitos=[0]*len(num)
    i=0
    j=len(num)-1
    for numero in num:
        digitos[i]=num[j]
        j=j-1
        i=i+1
    
    return digitos

for i in range(100, 5001):
    palind=palindromo(i)
    palind=''.join(palind)
    palind=int(palind)
    if palind == i:
        print(palind)        


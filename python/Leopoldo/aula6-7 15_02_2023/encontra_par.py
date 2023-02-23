def encontra_numero_par(L):
    for num in L:
        if num%2==0:
            return num
    raise ValueError('Não tem número par na lista')    

try:            
    encontra_numero_par([1,2,3,4,5])    
    encontra_numero_par([1,3,4,5])    
    encontra_numero_par([1,3,5])    
except ValueError:
    print('informou uma lista sem números pares')


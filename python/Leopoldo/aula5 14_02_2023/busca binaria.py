def busca_binaria(lista, low=, high, elemento):
    if high >= low:
        meio= (high+low)//2
        if lista[meio]==elemento:    
            return  meio
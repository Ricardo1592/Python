def ascendente(L):
    if len(L)<=1:
        return True
    return L[0] <= L[1] and ascendente(L[1:])
    
    """ continuar """
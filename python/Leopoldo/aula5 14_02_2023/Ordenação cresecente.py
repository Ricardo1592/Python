def ascendente(L):
    if len(L)<=1:
        return True
    return L[0] <= L[1] and ascendente(L[1:])


    
if __name__=="__main__":
    l1=[4,5,6,7,10,9]
    print(ascendente(l1))
letra=input()
letra=letra.upper()
letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def lista_vinicius(letras, letra):
    i=letras.index(letra)
    i=i+1
    letras=letras[:i]
    return letras
letras=lista_vinicius(letras, letra)
def lista_triangulo(letras, letra):
    ind=len(letras)
    i=(ind-1)*2+1
    tam=['.']*i
    meio=len(tam)//2
    j=(len(letras)-1)*2+1   
    if len(letras)>1:
        c=0
        for l in letras:
            tam[meio]=l
            if c>0:
                l2=letras[:c]
                l2.reverse()
                tam[(meio+1):(meio+c+1)]=l2
                tam[(meio-c):meio]=letras[:c]
                print(''.join(tam))
            else:
               tam[meio]=l
               print(''.join(tam))  
            c+=1            
        return tam    



    else:
        tam=['.']*3
        tam[1]=letra   
        return tam

lista_triangulo(letras, letra)


# antigo
#   i=len(tam)//2
#         tam[i]=letras[0]
#         letras=letras[:-1]
#         j=0
#         k=-1
#         for l in letras:
#             tam[j]=l
#             tam[k]=l
#             j+=1
#             k-=1
    
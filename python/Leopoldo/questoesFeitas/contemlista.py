def ContemLista(l1 :list, l2 :list):
    for e in l1:
        i=0
        elementosIguais=0
        j=l1.index(e)    
        if e==l2[i]:
            while j<len(l1) and i<len(l2) and l1[j]==l2[i]:
                i+=1
                j+=1
                elementosIguais+=1
        if elementosIguais==len(l2):
            return True
    return False    

l1=[1,2,3,4,5,6,7,8,10]
l2=[4,5,6]
l3=[3,4,5,6,7,8]   
print(ContemLista(l1,l3))      
       
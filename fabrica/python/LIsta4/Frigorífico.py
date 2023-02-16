n=int(input())
bois={}
def dict_ascendente(d :dict):
    dict_asc=[]
    values=d.values()
    values=list(values)
    values.sort()
    for value in values:
        for key in d:
            if value==d[key]:
                dict_asc=dict_asc+[(key, value)]                        
    # dict_asc=dict(dict_asc) # Dict de uma lista de tuple os transforma em key and value por indice da lista sem precisar do for 
    return dict_asc
for i in range(1, n+1):
    dados=input()
    dados=dados.split()
    id= int(dados[0])
    peso= float(dados[1])
    bois[id]=peso

asc= dict_ascendente(bois)
print("Gordo: id: {} peso: {:.2f}Kg".format(asc[-1][0], asc[-1][1]))
print("Magro: id: {} peso: {:.2f}Kg".format(asc[0][0], asc[0][1]))

n=int(input("Digite a quantidade de seções: "))
tabela={}
for i in range(1, n+1):
    itens=input("Digite os itens da seção %d : " %i)
    itens=itens.split(", ")
    tabela[i]=itens
print(tabela)

compras=input("Digite o produto e a seção: ")
tab_compras={}
while compras !='FIM':
    tem=False
    sec=int(compras.split(", ")[0])
    # print('sec -->', sec)
    compra=compras.split(", ")[1]
    # print('compra -->', compra)
    print(sec, compra)
    for key, value in tabela.items():
        # print(key, value)
        if key==sec and compra in value: 
            print('TEM')
            tem=True
    if not tem: print('Indisponível')
    tab_compras[sec]=compra
    compras=input("Digite o produto e a seção: ")   
print(tab_compras)    



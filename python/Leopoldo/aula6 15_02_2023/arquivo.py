with open ('nome.txt','w') as arq:
    for i in range(3):
        nome = input('Digite um nome:')
        arq.write(nome+'\n')
    print(arq)    
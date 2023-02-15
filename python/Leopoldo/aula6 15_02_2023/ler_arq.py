import sys

args=sys.argv
nome=r'%s' %(args[1])
print(nome)
maior=0
with open(nome, 'r') as arq:
    print(arq)
    conteudo=arq.readlines()
    print(conteudo)
    for i in conteudo:
        j=int(i)
        if j>maior:
            maior=int(i)
    print(maior)        
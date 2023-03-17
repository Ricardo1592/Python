# with open('valores.csv','r') as arq_leitura:
#     with open('valores.txt','w') as arq_escrita:
#         for linha in arq_leitura:
#             soma = 0
#             for num in linha.strip().split(','):
#                 soma = soma + int(num)
#             # print(linha.strip(), '=', soma)
#             # print( linha.split(','))
#             arq_escrita.write(str(soma)+'\n')

# with open('valores.csv','r') as arq_leitura:
#     with open('valores.txt','w') as arq_escrita:
#         for linha in arq_leitura:
#             # soma = sum(map(int,linha.split(',')))
#             soma = sum([int(e) for e in linha.split(',')])
#             arq_escrita.write(str(soma)+'\n')

import csv
with open('valores.csv','r') as arq_leitura:
    with open('valores.txt','w') as arq_escrita:
        reader = csv.reader(arq_leitura)
        for linha in reader:
            # soma = sum(map(int,linha.split(',')))
            soma = sum([int(e) for e in linha])
            arq_escrita.write(str(soma)+'\n')
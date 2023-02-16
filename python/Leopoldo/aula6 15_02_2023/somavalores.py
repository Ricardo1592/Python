lista=[]
with open (r'C:\Users\rcmm\Desktop\residência\Residencia_robotica\Residencia_robotica\python\Leopoldo\aula6 15_02_2023\valores.csv') as arq:
    with open('valores.txt', 'w') as arq_escrita:
        for linha in arq:
            # soma=0
            # for num in linha.strip().split(","):
            #     soma = soma + int(num)
            #         #OU
            # soma = sum(map(int, linha.split(',')))
            # arq_escrita.write(str(soma) + '\n')        
            # print(soma)
                    #OU
            arq_escrita.write(str(sum([int(num) for num in linha.split(',')])) + '\n')



import csv

empregados = {}
# empregados['080488-123X'] = {}
# empregados['080488-123X']['nome'] = 'Teste Nome'
# empregados['080488-123X']['endereco'] = 'Av. Recife 127'
# empregados['080488-123X']['cidade'] = 'Recife'
# E_ID = '080488-123X'
# print(empregados[E_ID]['nome'])

with open('empregados.csv') as f:
    reader = csv.reader(f,delimiter=';')
    for l in reader:
        if l[0] == 'id':
            continue
        ID = l[0]
        NOME = l[1]
        ENDERECO = l[2]
        CIDADE = l[3]
        empregados[ID] = {}
        empregados[ID]['nome'] = NOME
        empregados[ID]['endereco'] = ENDERECO
        empregados[ID]['cidade'] = CIDADE

with open('salarios.csv') as f:
    reader = csv.reader(f,delimiter=';')
    for l in reader:
        if l[0] == 'id':
            continue
        ID = l[0]
        SALARIO = l[1]
        BONUS = l[2]
        # empregados[ID] = {}
        empregados[ID]['salario'] = int(SALARIO)
        empregados[ID]['bonus'] = int(BONUS)

for id, empregado in empregados.items():
    NOME = empregado['nome']
    if 'salario' in empregado and 'bonus' in empregado:
        SALARIO = empregado['salario'] + empregado['bonus']
        msg = f'{NOME} tem o salário com bônus de R${SALARIO}'
    else:
        msg = f'Não temos informação de salário para {NOME}'
    
    print(msg)
    print()
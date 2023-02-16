n=int(input())
class Aluno():

    def __init__(self, codigo :str, nome :str, idade :int, sexo :int, nota :float):
        self.codigo= codigo[:31]
        self.nome=nome[:501]
        self.idade=idade  
        self.sexo=sexo # 1-masculino
        self.nota=nota 

alunos=[]
for i in range(1, n+1):
    codigo=input() 
    nome=input()
    idade=int(input())
    sexo=int(input()) 
    nota=float(input())
    aluno=Aluno(codigo, nome, idade, sexo, nota)
    alunos.append(aluno)

qtd_masc=0
qtd_fem=0
soma_idade=0
soma_notas=0
qtdNotas=0
for aluno in alunos:
    if aluno.sexo == 1:
        qtd_masc+=1
    if aluno.sexo == 0:
        qtd_fem+=1    
    soma_idade=soma_idade + aluno.idade
    if aluno.nota>7.5:
        soma_notas=soma_notas + aluno.idade
        qtdNotas=qtdNotas+1

media_idade=soma_idade/len(alunos)
media_idade="%.2f" %media_idade
if qtdNotas>0: 
    media_notas=soma_notas/qtdNotas

else: 
    media_notas=0 

# OK ESSA PARTE
disciplinas={}
m=int(input())    
for i in range (m):
    cod_disciplina=input()
    cod_disciplina=cod_disciplina[:26]
    disciplina=input()
    disciplina=disciplina[:101]
    disciplinas[cod_disciplina]=[disciplina]

# print(disciplinas)

def ordena_disciplina(disciplinas :dict):
    disciplinas_lista=[]
    for key in disciplinas:
        dis=disciplinas[key][0].lower()
        disciplinas_lista.append(dis)
    disciplinas_lista.sort()    
    return disciplinas_lista
# print(ordena_disciplina(disciplinas))

p=int(input())
for i in range(p):
    cadastro=input()
    aluno_cod = cadastro.split()[0]
    dCod = cadastro.split()[1]
    for aluno in alunos:
        if aluno.codigo==aluno_cod and aluno.nome not in disciplinas[dCod] and dCod in disciplinas:
            # print('cadastrando aluno: ', aluno.nome)
            disciplinas[dCod]=disciplinas[dCod]+[aluno.nome]


disp_ordenado=ordena_disciplina(disciplinas)
print(qtd_masc)
print(qtd_fem)
print(media_idade)
print("%.2f" %media_notas)
for disp in ordena_disciplina(disciplinas):
    for key in disciplinas:
        if disciplinas[key][0].lower()==disp:
            print(disciplinas[key][0])
            print(len(disciplinas[key])-1)
            lista_alunos=disciplinas[key][1:]
            lista_alunos.sort()
            for aluno in lista_alunos:
                print(aluno)
            # print("qtd de alunos em {} é {}".format(disciplinas[key][0], len(disciplinas[key])-1))
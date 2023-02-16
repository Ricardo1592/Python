seçao= int(input())
qtd_votosA=0
qtd_votosB=0
qtd_votosC=0
qtd_brancos=0
qtd_nulos=0
segundoT=True
valida=True
i=0
while seçao > 0:
    votosA=int(input())
    votosB=int(input())
    votosC=int(input())
    brancos=int(input())
    nulos=int(input())

    qtd_votosA=qtd_votosA + votosA
    qtd_votosB=qtd_votosB + votosB
    qtd_votosC=qtd_votosC + votosC
    qtd_brancos=qtd_brancos+brancos
    qtd_nulos=qtd_nulos+nulos
    
    seçao= int(input())
    i=i+1

votantes= qtd_votosA + qtd_votosB + qtd_votosC +qtd_nulos +qtd_brancos   
validos= votantes - qtd_brancos - qtd_nulos   
if validos/2<=qtd_votosA or validos/2<=qtd_votosB or validos/2<=qtd_votosC:
    segundoT=False
if qtd_brancos+ qtd_nulos >= validos:
    valida=False

maior=qtd_votosA
if i>0:
    candidato='A'
else:
    candidato=''    
if qtd_votosB>maior:
    maior=qtd_votosB
    candidato='B'
if qtd_votosC>maior:
    maior='C'
    candidato='C'   
if qtd_votosA==qtd_votosB==qtd_votosC:
    candidato=''    
print("Numero de votantes:", votantes)    
print("Total A:", qtd_votosA)    
print("Total B:", qtd_votosB)    
print("Total C:", qtd_votosC)    
print("Brancos:", qtd_brancos)    
print("Nulos:", qtd_nulos)    
print("Validos:", validos)    
print("Candidato mais votado:", candidato)    
print("Eleicao valida?", valida)
print("Segundo turno?", segundoT)

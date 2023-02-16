votosA=int(input())
votosB=int(input())
votosC=int(input())
Nulos=int(input())
total=votosA+votosB+votosC+Nulos
pA=(votosA/total)*100
pB=(votosB/total)*100
pC=(votosC/total)*100
pNulos=(Nulos/total)*100

print('Digite a quantidade de votos do candidato A:')
print('Digite a quantidade de votos do candidato B:')
print('Digite a quantidade de votos do candidato C:')
print('Digite a quantidade de votos nulos:')
print('Candidato A: %s' % ('%.3f' %(pA) + ' %'))
print('Candidato B: %s' % ('%.3f' %(pB) + ' %'))
print('Candidato C: %s' % ('%.3f' %(pC) + ' %'))
print('Votos Nulos: %s' % ('%.3f' %(pNulos) + ' %'))
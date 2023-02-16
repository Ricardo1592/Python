anos=input()
ano1, ano2= map(int, anos.split())
sem_bis=0
for ano in range(ano1, ano2+1):
    if ano%100==0 and ano%400==0:
        bissexto= ano
        sem_bis=sem_bis+1
        print(bissexto)
    if ano%4 == 0 and ano%100!=0:
        bissexto= ano
        sem_bis=sem_bis+1
        print(bissexto)

if sem_bis==0:
    print(-1)
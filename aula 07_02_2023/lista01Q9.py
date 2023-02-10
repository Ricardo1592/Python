# Calcular o n-ésimo termo da sequência --> -1,0,5,6,11,12,17,18,....
n= int(input('Digite do n-esimo termo:'))
termo=-1
i=1
while i <= n:
    termoN=termo 
    # print("termo", i, "é:",termo) 
    if i%2!=0:
        termo= termo+1
    else:
        termo=termo+5   
    i=i+1        
print("O termo ", n ,"é:", termoN)

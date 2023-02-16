numeros=input()
cap, juros, anos= map(float, numeros.split())
anos=int(anos)
tempo=anos*4
mont=cap
rendimento=0
for i in range(tempo):
    rendimento=mont*juros
    mont=mont+ mont*juros
    print("Rendimento: %.2f Montante: %.2f" %(rendimento, mont))

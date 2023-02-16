total_sec=0
total_min=0

for i in range(1,6):
    min=int(input())
    sec=int(input())
    total_sec=total_sec+sec
    total_min=total_min+min

secTOmin=total_sec//60
total_min=total_min + secTOmin
horas=total_min//60
resto_sec=total_sec%60

print(horas)
print(total_min)
print(resto_sec)
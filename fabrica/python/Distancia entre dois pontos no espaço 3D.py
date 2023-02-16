import math
p1=input()
p2=input()
p1x, p1y, p1z=map(float, p1.split())
p2x, p2y, p2z=map(float, p2.split())

soma=(p1x - p2x)**2 + (p1y - p2y)**2 + (p1z - p2z)**2
distancia=math.sqrt(soma) 
print("%.2f" %(distancia))   
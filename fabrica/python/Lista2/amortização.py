
f=float(input())
n=int(input())
t=float(input())

denominador=((1+t)**n -1)/((t*(t+1)**n))
p=f/denominador
print(int(p))

nm=input()
n,m = map(int, nm.split())

dominos=0
if m>=1 and n<=16:
    dominos= n*m//2
print(dominos)    


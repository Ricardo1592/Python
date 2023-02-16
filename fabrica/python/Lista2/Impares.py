num=int(input())
while num>0:
    if num%2!=0:
        quad1=(num+1)/2
        quad2=quad1-1
        print("%d - %d" %(quad1**2, quad2**2))
    num=int(input())

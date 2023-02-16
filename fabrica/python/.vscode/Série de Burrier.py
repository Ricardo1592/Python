n=int(input())

def burrier(n):
    pi=3.14
    for t in range(n):
        if t%2!=0:
            termo= pi*(n-1*t)/(2**t)
            print(termo)
        else:
            termo=t*(n**t)
            print(termo)
burrier(n)

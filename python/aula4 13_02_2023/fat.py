num=int(input())
def fat(num):
    if num<2:
        f=1
        print(f)
    else:
        f=num*fat(num-1)
        print(num)
    return f

print(fat(num))
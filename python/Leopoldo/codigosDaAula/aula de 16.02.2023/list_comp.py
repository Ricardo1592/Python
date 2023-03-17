L = ['1','2','3','4']
def add_espaco(s):
    return s+' '
print(L)
print(list(map(add_espaco, L)))
print(L)
I = list(map(int, L))
print(I)
print(list(map(lambda x:x+1,I)))
print([x+1 for x in I])
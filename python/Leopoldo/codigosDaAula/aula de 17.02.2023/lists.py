L = [1,2,3]
M = L.copy()
print(type(L), type(M), type(L[0]), type(L[1]))
print(L, M)
M.append(4)
print(L, M)
print('----')
L = [[1],[2],[3]]
M = L.copy()
print(type(L), type(M), type(L[0]), type(L[1]))
print(L, M)
M[0].append(4)
print(L, M)


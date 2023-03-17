#Escreva uma função que recebe uma lista L e 
#  devolve uma nova lista sem elementos duplicados

# def removerDuplicados(L):
#     N = []
#     for e in L: 
#         if e not in N:
#             N.append(e)
#     return N
# def removerDuplicados(L):
#     S = set()
#     for e in L: 
#         if e not in S:
#             S.add(e)
#     return list(S)
# def removerDuplicados(L):
#     # L.sort()
#     # return [L[i] for i in range(len(L)) if L[i]!=L[i-1]]
#     # return [i for i in set(L)]
#     return list(set(L))
# print(removerDuplicados([1,1,1,1,1,2,3,2,3,2,3,2,3,2,1,2,4]))

#Escreva uma função que recebe duas listas e 
#  retorna True caso tenham elementos em comum

# def temElementosEmComum(L1,L2):
#     for e in L1:
#         if e in L2: 
#             return True
#     return False
# def temElementosEmComum(L1,L2):
#     # S1 = set(L1)#L1=[1,1,1,2,3,2,4] set(L1)={1,2,3,4}
#     # S2 = set(L2)
#     return len(set(L1).intersection(set(L2)))>0
    
# print(temElementosEmComum([1,2,3],[4,5,6]))

#Escreva uma função que recebe uma lista L e outra lista S 
# e retorna True caso S seja uma sublista de L

def sublista(L,S):
    sub_lista = False
    if S == []:
        sub_lista = True
    elif S == L: 
        sub_lista = True
    elif len(S)>len(L):
        sub_lista = False
    else:
        for i in range(len(L)):
            if L[i]==S[0]:
                n = 1
                while (n<len(S)) and (i+n<len(L)) and (L[i+n] == S[n]):
                    n+=1
                if n == len(S):
                    sub_lista = True
    
    return sub_lista
                    
# print(sublista([1,2,3,4,5,6,7,8,9,10],[2,3])) #True
# print(sublista([1,2,3,4,5,6,7,8,9,10],[2,6])) #False
# print(sublista([1,1,1],[1,1,1,1,1,1])) #False
# print(sublista([1,1,1],[1])) #True
# print(sublista([4,1,2,3],[2,3,4]))


#Escreva uma função que recebe uma string s como argumento
# e retorna um dicionário com a frequência de cada letra 
# nesta string. Por ex. frequenciaLetras('leopoldo') retorna 
# {'l':2,'e':1,'o':3,'p':1,'d':1}
# frequenciaLetras('Leopoldo') -> {'L':1,'l':1,'e':1,'o':3,'p':1,'d':1}

# def frequenciaLetras(s): 
#     s = s.upper()#s.lower()
#     frequencia = {}
#     for letra in s: 
#         frequencia[letra] = 0
#     for letra in s: 
#         frequencia[letra]+=1
# def frequenciaLetras(s): 
#     s = s.lower()
#     frequencia = {}
#     for letra in s: 
#         if letra not in frequencia: 
#             frequencia[letra] = 1
#         else: 
#             frequencia[letra]+=1
#     return frequencia
def frequenciaLetras(s):
    frequencia = {}
    for letra in set(s):
        frequencia[letra] = s.count(letra)
    return frequencia

print(frequenciaLetras('leopoldo'))
print(frequenciaLetras('Leopoldo'))

#Escreva uma função que recebe um nome de arquivo como argumento
# e conta a quantidade de palavras neste arquivo
# def contarPalavras(arquivo):
#     f = open(arquivo,'r')
#     texto = f.read()
#     f.close()
#     palavras = texto.split()
#     return len(palavras)
def contarPalavras(arquivo):
    with open(arquivo) as f:
        texto = f.read()
        palavras = texto.split()
        return len(palavras)
print(contarPalavras('lorem-20.txt'))
print(contarPalavras('lorem-200.txt'))

# Crie uma classe Loja, que vai guardar dados como o estoque 
# de produtos (nome do item, preço, e quantidade disponível),
# assim como um histórico dos pedidos realizados
# A classe deve dar suporte às seguintes operações:
# - Adicionar item ao estoque 
# - Vender item (receber o nome o item e a quantidade vendida)
#   * A quantidade em estoque deve ser atualizada de acordo
# - Imprimir produtos ainda em estoque
# - Imprimir produtos fora de estoque
# - Calcular receita obtida com vendas, com base no histórico

class Loja:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.__estoque = {}
        self.__pedidos = []
    def adicionarProduto(self,nome,valor,quantidade): 
        self.__estoque[nome] = {'valor':valor, 'qtde':quantidade}
    def vender(self,nome,quantidade):
        produto = self.__estoque[nome]
        valorProduto = produto['valor']
        estoqueAtual = produto['qtde']
        self.__estoque[nome]['qtde']-= quantidade
        self.__pedidos.append({'nome':nome, 'qtde':quantidade, 'valorTotal':valorProduto*quantidade})
    def imprimirEmEstoque(self):
        for nome, produto in self.__estoque.items(): 
            if produto['qtde']>0:
                valor = produto['valor']
                qtde = produto['qtde']
                print(f'{nome}, R${valor} | {qtde} unidade(s)')
    def imprimirForaEstoque(self):
        for nome, produto in self.__estoque.items(): 
            if produto['qtde']<=0:
                valor = produto['valor']
                qtde = produto['qtde']
                print(f'{nome}, R${valor}')
    def totalVendas(self):
        receita = 0
        for pedido in self.__pedidos:
            receita+=pedido['valorTotal']
        return receita
    
loja = Loja('teste')
print('---')
print('Produtos em estoque')
loja.imprimirEmEstoque()
print('---')
print('Produtos fora de estoque')
loja.imprimirForaEstoque()
print('---')
print(f'A loja {loja.nome} já vendeu R${loja.totalVendas()}')
print('---')
loja.adicionarProduto('bola',30,2)
loja.adicionarProduto('tenis',50,12)
loja.adicionarProduto('short',40,1)
print('---')
print('Produtos em estoque')
loja.imprimirEmEstoque()
print('---')
print('Produtos fora de estoque')
loja.imprimirForaEstoque()
print('---')
print(f'A loja {loja.nome} já vendeu R${loja.totalVendas()}')
print('---')
loja.vender('bola',2)#60
loja.vender('short',1)#40
loja.vender('tenis',2)#100
print('---')
print('Produtos em estoque')
loja.imprimirEmEstoque()
print('---')
print('Produtos fora de estoque')
loja.imprimirForaEstoque()
print('---')
print(f'A loja {loja.nome} já vendeu R${loja.totalVendas()}')
print('---')

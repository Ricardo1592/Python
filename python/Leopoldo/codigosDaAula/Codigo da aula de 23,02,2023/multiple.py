class X(object):
    def __init__(self):
        print('X')

class Y(object):
    def __init__(self):
        print('Y')

class A(X):
    def __init__(self):
        print('A')

class B(Y):
    def __init__(self):
        print('B')

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C')

if __name__=='__main__':
    c = C()
    # print(type(c))
    # print(isinstance(c,A))
    # print(isinstance(c,B))
    # print(isinstance(c,C))
    print(C.__mro__)
    # print(str(c))
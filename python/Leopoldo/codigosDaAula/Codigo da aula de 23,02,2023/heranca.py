class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass

if __name__=='__main__':
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    print(type(c))
    print(type(c)==A)
    print(type(c)==C)
    # print(isinstance(a,(B,C,D,E)))
    print(type('ab'))
    print(type(str))
    
    print(isinstance('ab',str) == isinstance(str,str))
    # print(isinstance(a,A))
    # print(isinstance(a,B))
    # print(isinstance(a,C))
    # print(isinstance(a,D))
    # print(isinstance(a,E))
    
    
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(type(a))
    # print(type(b))
    # print(type(c))
    # print(type(d))
    # print(type(e))
    
    # print(isinstance(a,A))
    # print(isinstance(b,A))
    # print(isinstance(c,A))
    # print(isinstance(d,A))
    # print(isinstance(e,A))
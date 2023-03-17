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

a = A()
b = B()
c = C()
d = D()
e = E()
print(a)
print(b)
print(c)
print(d)
print(e)
print(isinstance(a,A))
print(isinstance(b,A))
print(isinstance(c,A))
print(isinstance(d,A))
print(isinstance(e,A))
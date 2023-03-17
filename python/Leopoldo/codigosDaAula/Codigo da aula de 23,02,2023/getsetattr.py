class A:
    def __init__(self):
        self.x = 12
        self.y = 13

a = A()
# print(a.x)
# print(a.y)
print(getattr(a,'z')) # a.x
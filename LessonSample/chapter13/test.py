class A:
    pass

class B:
    def __init__(self, name, age):
        print 'B __init__'
        self.name = name
        self.age = age

class C(A, B):
    pass

c = C('a',45)



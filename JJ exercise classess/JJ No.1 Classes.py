class object :
    pass

class X(object):
    pass

class Y(object):
    pass

class Z(object):
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(A,B,Z):
    pass

ayo = object()
ayo1 = X()
ayo2 = Y()
ayo3 = Z()
ayo4 = A()
ayo5 = B()
ayo6 = M()

print(isinstance(ayo, object))

print(isinstance(ayo1, X))
print(isinstance(ayo1, object))

print(isinstance(ayo2, Y))
print(isinstance(ayo2, object))

print(isinstance(ayo3, Z))
print(isinstance(ayo3, object))

print(isinstance(ayo4, A))
print(isinstance(ayo4, X))
print(isinstance(ayo4, Y))
print(isinstance(ayo4, object))

print(isinstance(ayo5, B))
print(isinstance(ayo5, Y))
print(isinstance(ayo5, Z))
print(isinstance(ayo5, object))

print(isinstance(ayo6, M))
print(isinstance(ayo6, A))
print(isinstance(ayo6, B))
print(isinstance(ayo6, X))
print(isinstance(ayo6, Y))
print(isinstance(ayo6, Z))
print(isinstance(ayo6, object))
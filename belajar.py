def f(x):
    return x**2
def g(x):
    return x-2
def h(x):
    return x+1
def fogoh(x):
    return f(g(h(x)))
def gohof(x):
    return g(h(f(x)))
def hofog(x):
    return h(f(g(x)))

a, b, c = map(int, input().split())

print(fogoh(a))
print(gohof(b))
print(hofog(c))

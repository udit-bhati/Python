def gencubes(n):
    for num in range(n):
        yield num**3

x = gencubes(3)
print(next(x))
print(next(x))
print(next(x))
# print(next(x))

def fibon(n):
    a = 0
    b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

for num in fibon(10):
    print(num)



s = 'hello'

for l in s:
    print(l)

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
# print(next(s_iter))
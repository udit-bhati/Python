def gen_square(n):
    for i in range(n):
        yield i**2

for x in gen_square(10):
    print(x)


import random

def rand_num(low, high, n):
    
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


s = 'hello'

s_iter = iter(s)

print(next(s_iter))


my_list = [1,2,3,4,5]

def gen():
    for i in my_list:
        if i > 3:
            yield i

for i in gen():
    print(i)


# Using generator comprehension
my_list2 = [1,2,3,4,5]

gencomp = (i for i in my_list2 if i > 3)

for item in gencomp:
    print(item)
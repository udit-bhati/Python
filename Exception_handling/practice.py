try:
    for i in ['a','b']:
        print(i**2)
except TypeError:
    print("Unsupported operation")



X = 5
Y = 0
try:
    Z=X/Y
    print(int(Z))
except ZeroDivisionError:
    print("Infinite is the answer")
finally:
    print('Calculation Completed.')



def func():
    while True:
        try:
            num = int(input('Enter a number : '))
        except:
            print('Oops! that is not a number')
            continue
        else:
            break
    sqr = num**2
    print(f'Square of {num} =',sqr)

func()
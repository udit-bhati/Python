def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome

# hi = hello('who')
# print(hi())


def func():
    print("Hi Udit!")

def other_func(other):
    print("This is output of other func")
    print(other())

# other_func(func)


def new_decorator(other):

    def wrap_func():
        print("Code would be here, before executing the func")

        other()

        print("Code here will execute after the func()")

    return wrap_func

# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# func_needs_decorator()
# hello = new_decorator(func_needs_decorator)
# hello()


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
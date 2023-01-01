# def myfunc(*args):
#     out = []
#     for item in args:
#         if item%2==0:
#             out.append(item)
#     print(out)

# myfunc(2,3,4,5,6,7,8)

# def myfunc(a):
#     out = []
#     for item in range(len(a)):
#         if item%2 == 0:
#             out.append(a[item].lower())
#         else:
#             out.append(a[item].upper())
#     return ''.join(out)

# print(myfunc('abcde'))



def myfunc(word):
    new_string = ''
    counter = 0

    for letter in word:
        if counter % 2 == 0:
            new_string = new_string + word[counter].lower()
            counter+=1
        else:
            new_string = new_string + word[counter].upper()
            counter+=1

    return new_string

print(myfunc('abcde'))
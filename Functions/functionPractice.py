# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

# My solution :
# def myfunc(a,b):
#     first_num=True
#     second_num=True
#     if a%2==0:
#         first_num = True
#     else:
#         first_num = False

#     if b%2==0:
#         second_num = True
#     else:
#         second_num = False
    
#     if ((first_num == True) and (second_num == True)):
#         print(min(a,b))
#     else:
#         print(max(a,b))

# myfunc(2,5)


# Udemy Solution :
# def lesser_of_two_evens(a,b):
#     if a%2==0 and b%2==0:
#         return min(a,b)
#     else:
#         return max(a,b)
# print(lesser_of_two_evens(2,4))


# -------------------------------------------------***********-------------------------------------------


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True 
# if both words begin with same letter

# def animal_crackers(text):
#     words = text.split()
#     return words[0][0].lower() == words[1][0].lower()
# print(animal_crackers('Levelheaded Llama'))


# -------------------------------------------------***********-------------------------------------------


# MAKES TWENTY: Given two integers, 
# return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# 
# my solution
# def makes_twenty(a,b):
#     if a==20 or b==20 or a+b == 20:
#         return True
#     else:
#         return False

# udemy
# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20

# print(makes_twenty(10,8))


# -------------------------------------------------***********-------------------------------------------


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'
# print(old_macdonald('abcd'))

# print('hellPPP'.capitalize())


# -------------------------------------------------***********-------------------------------------------


# MASTER YODA: Given a sentence, return a sentence with the words reversed

# def master_yoda(sentence):
#     return ' '.join(sentence.split()[::-1])

# print(master_yoda('I am here'))

# -------------------------------------------------***********-------------------------------------------

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(a):
#     return ((abs(100 - a) <= 10) or (abs(200 - a) <= 10))

# print(almost_there(101))


# -------------------------------------------------***********-------------------------------------------


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def find_33(nums):
#     for i in range(0, len(nums)-1):
#         # if nums[i] == 3 and nums[i+1] == 3:
#         if nums[i:i+2] == [3,3]:
#             return True
#     return False

# print(find_33([1,2,3,3,4,5]))


# -------------------------------------------------***********-------------------------------------------


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# def paper_doll(letter):
#     result=''
#     for char in letter:
#         result += char*3
#     return result

# print(paper_doll('abcd'))


# -------------------------------------------------***********-------------------------------------------

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# def blackjack(a,b,c):
#     if sum((a,b,c)) <= 21:
#         return sum((a,b,c))
#     elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
#         return sum((a,b,c))-10
#     else:
#         return 'BUST'

# print(blackjack(11,11,10))


# -------------------------------------------------***********-------------------------------------------

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total

# print(summer_69([2,1,6,9,11]))


# -------------------------------------------------***********-------------------------------------------


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# def spy_game(nums):

#     code = [0,0,7,'x']
    
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
       
#     return len(code) == 1

# print(spy_game([1,2,4,0,0,5,7]))


# -------------------------------------------------***********-------------------------------------------


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3,x,2):  # test all odd factors up to x-1
#             if x%y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)

# print(count_primes(100))

# -------------------------------------------------***********-------------------------------------------

# Just for fun, not a real problem :)
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])

# print_big('a')
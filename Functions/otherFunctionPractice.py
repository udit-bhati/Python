

# -------------------------------------------------***********-------------------------------------------
# Write a function that computes the volume of a sphere given its radius.
from math import pi

def vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(vol(2))


# -------------------------------------------------***********-------------------------------------------
# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

ran_check(8,2,7)

def ran_bool(num,low,high):
    return num in range(low,high+1)

print(ran_bool(8,2,7))


# -------------------------------------------------***********-------------------------------------------
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
from curses.ascii import isupper

def up_low(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        else:
            pass
    print(upper_count, lower_count)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# -------------------------------------------------***********-------------------------------------------
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]))


# -------------------------------------------------***********-------------------------------------------
# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,-4]))


# -------------------------------------------------***********-------------------------------------------
# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    s = s.replace(' ', '')
    return s.lower() == s[::-1].lower()

print(palindrome('nurses run'))


# # -------------------------------------------------***********-------------------------------------------
# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    # Create a set of the alphabet
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation 
    str1 = str1.lower()
    
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    
    # Now check that the alpahbet set is same as string set
    return str1 == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))
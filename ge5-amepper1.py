"""
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""

#Answer to Question 1
def is_prime(num):
    result = True
    if num > 1:
        for i in range(2, num):
# check for divisors
            if num % i == 0:
                result = False
                break
    else:
        result = False
    return result

#Answer to Question 2
A = {i : round(((i*(9/5))+32),1) for i in range(0, 36)}
# Printing the temperatures
print(A)

#Answer to Question 3

#Answer to Question 4
def get_char_count_dict(txt):
    if type(txt) == str:
        txt = txt.lower()
        D = {}
        for key1 in txt:
            count = txt.count(key1)
            D[key1] = count      
        return D
    else:
        return -1

#Answer to Question 5
tups = [('English', 88), ('Science', 90), ('Maths', 97), ('History', 82)]
result = sorted(tups, key = lambda x: x[1])
print(result)

#Answer to Question 6
# randint returns an integer number selected element from the specified range, random.randint(start, stop), randrange(start, stop+1), arguments are start and stop, print(random.randint(3, 9))
import random
def lottery(n=6):
    for i in range(n):
        yield(random.randint(0,41))


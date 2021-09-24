"""
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
#Answer to Question 1

a = 1
b = 2
c = 3.1
result1 = a+b+c

print(type(result1))
print(result1)


#Answer to Question 2
string1= "This is a longer string\nthat spans multiple lines"
print(string1.count("s"))

#Answer to Question 3
import math
var1=math.pi
print(round(var1,3))

#Answer to Question 4
var1 = int(input('Enter a var1 number: '))
var2 = int(input('Enter a var2 number: '))

var3= var1*var2

print('')
print('The result of multiplying var1 and var2 is:', var3)

#Answer to Question 5
numerator1 = '32000'
denominator1 = '1000'
print(float(numerator1)/float(denominator1))

#Answer to Question 6
year = 1991
author = 'Guido van Rossum'
text1 = "Python is a general-purpose programming language released in " + str(year) + " "+ author
print(text1)

#Answer to Question 7
sunny = True
warm = False
print('Is it True or False that I should go out for ice cream?:', (sunny and warm))

#when you have "and" with boolean statements and one is false then the output will always be false
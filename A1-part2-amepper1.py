"""
@description: Answer to Part 2 of Programming Assignment 1
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
import collections
from collections import Counter
#2.4.1
#The read() method returns the specified number of bytes from the file
#Syntax: file.read()
f = open("app-review.txt", "r")
print(f.read(33)) #will print the first 33 bits
#2.4.2
#A Counter is a dict subclass for counting hashable objects. 
#It is a collection where elements are stored as dictionary keys 
#and their counts are stored as dictionary values. Counts are allowed
#to be any integer value including zero or negative counts.
#syntax: class collections.Counter([iterable-or-mapping])
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
#2.4.3
#syntax: most_common([n])
#Return a list of the n most common elements and their counts from the most common to the least.
Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)] # output is [('a', 5), ('b', 2), ('r', 2)]

#2.5.1
path= "app-review.txt" # assigns file path to variable
dataFile = open(path, "rt")#assigns/stores path to variable
dataFile.close()#close()the input file

with open(path, 'r') as fileinput:
   for line in fileinput:  #for everyline in file
       line = line.lower() # make the line contents lowercase
def remove_punctuations(old_str):
    punctuations = '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~' # all variations of puncuations 
    new_str = ''.join( filter(lambda x: x not in punctuations, old_str) )
    return new_str
"""
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
#Answer to Question 1
lsta = ['c', 'b', 'a']
lstb = [3, 2, 1]

dicta = {}
for a,b in zip(lsta, lstb):
    dicta[a]=b

print(dicta)

#Answer to Question 2
dict1 = {'e': 2, 'j': 4, 'a': 3, 't': 6, 'q': 1}
for elem in sorted(dict1.items(), reverse=True) :
    print("key :",elem[0], "; value :" , elem[1] )

#Answer to Question 3
lorem = 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip'
lorem_words = lorem.split()
print(lorem_words)

word_len={}

for i in sorted(lorem_words):
        word_len[i]=len(i)

print(word_len)

#Answer to Question 4
mylist = ['action', 'table', 'tennis', 'apple', 'trap']
dictA={}

for i in mylist:
        x=dictA.setdefault(i[0],[])
        dictA[i[0]]=x+[i]

print(dictA)

#Answer to Question 5
chars = 'immunoelectrophoretically'
char_count = {}
for c in chars:
    if c in char_count:
         char_count[c] += 1
    else:
         char_count[c] = 1

print('Character count:', char_count)

#Answer to Question 6
from collections import defaultdict
chars = 'immunoelectrophoretically'

char_count2 = defaultdict(int)

for c in chars:
    char_count2[c] +=1


print('Character count:', char_count2)

#Answer to Question 7
A = set(range(2, 21, 2))
B = set(range(5, 21, 5))

U = A.union(B)
I = A.intersection(B)
S = U.difference(I)

print('U:', U)
print('I:', I)
print('S:', S)
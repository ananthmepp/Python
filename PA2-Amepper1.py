"""
@description: Answer to Programming Assignment 2 
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
import numpy as np
import pandas as pd
#QUESTION 1
#1 the attributes of the fish class are first_name and last_name
#2 the methods in the class fish are swim() andswim_backwards()
#3 class fish is the parent class
#4 Blue Tang child class
#5 here an object is created here, which takes an argument, Tropical.
#6 object obj initiated with class Fish, then it can access to the attribute of class Fish(firstname and lastname), obj.first_name prints Tropical and obj.last_name prints Fish. then the object Dory initiated with class BlueTang, it can also access the methods and attributes of both BlueTang and Fish
#7 when executed the method from parent class Fish accesses it prints "The fish is swimming"

#Question 2
class BankAccount:
    def __init__(self, name, amount):
        self.account_name = name
        self.account_balance = amount
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
class BankAccount2(BankAccount):
    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
        else:
            print('Insufficient funds')
    def balance(self):
        return self.account_balance

#Question 3
lst = [[1,2,3], [4,5,6]]
# when you multiply lst by 2 the output is [[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]
lst_np = np.array(lst)
#when lst_np is multiplied by 2 the output will be [[2,4,6][8,10,12]]
#Shape of lst_np is 2 rows and 3 columns
lst_np2 = lst_np.reshape(3,2)

#Question 4
#1
def my_random_integers(sd,sz):
    my_rng = np.random.default_rng(seed=sd)
    sample = my_rng.integers(1,1000,size=sz)
    return(sample)

#2 
# It returns the count of all the non zero values in the given function.
# numpy.count_nonzero(a, axis=None, keepdims=False)
# aarray_like: The array for which to count non-zeros.
# axisint or tuple, optional: Axis or tuple of axes along which to count non-zeros. Default is None
# keepdimsbool, optional: If this is set to True, the axes that are counted are left in the result as dimensions with size one.
a = np.array([[0, 0, 74, 0],
              [31, 44, 23, 194]])
print(np.count_nonzero(a,keepdims=True))
print(np.count_nonzero(a))

#3
def my_random_integers(sd,sz):
    my_rng = np.random.default_rng(seed=sd)
    sample = my_rng.integers(1,1000,size=sz)
    return(sample)
def percent_equal(arr1,arr2):
    if(arr1.shape == arr2.shape): #comparing shapes of arrays
        z = arr1 == arr2     
        count = np.count_nonzero(z)        # using count_nonzero
        try:
            xyz = x.shape[1]
        except:
            xyz = 1
        result = count / (arr1.shape[0] * xyz)
        return(result)
    else:
        return(-1)
    
#arr1 = np.array(([1,2,3],[7,8,9]))
#arr2 = np.array(([1,0,0],[0,0,9]))
#result = percent_equal(arr1,arr2)
#print(result)
#4 the random numbers are the same because they all have the same seed size

#Question 5
data = [2,7,2,0,9,5,5,np.nan,2,np.nan,1,0]
labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

s1 = pd.Series(data,index = labels)

q5ans1 = s1.values
q5ans2 = s1.index
q5ans3 = s1.dtypes
q5ans4 = s1['Mar']
s1['Dec'] = 4
q5ans6 = pd.Series([s1['Mar'],s1['Jun'],s1['Sep']])
q5ans7 = s1["Apr":"Sep"]
q5ans8 = s1.loc[s1 < 5]
q5ans9 = 'Mon' in s1.index
q5ans10 = s1[~(s1.index.isin(['Jul','Aug']))]
q5ans11 = s1.sort_index()
q5ans12 = s1.sort_index(ascending=False)
q5ans13 = s1.median()
q5ans14 = s1.idxmax()
q5ans15 = s1.value_counts()
q5ans16 = s1.isna().sum()
q5ans17 = s1.dropna()
q5ans18 = s1.fillna(-1)
q5ans19 =   s1.notna()
q5ans20 = s1.apply(lambda x : x**2)

#Question 6
data = { 'total_bill': [15.69, 16.49, 18.78, 9.94, 24.08, 14.52, 15.98, 40.17, 20.49, 20.27],
'tip': [1.5, 2.0, 3.0, 1.56, 2.92, 2.0, 3.0, 4.73, 4.06, 2.83],
'day': ['Sun','Sun','Thu','Sun','Thu','Thu','Fri','Fri','Sat','Thu'],
'time': ['Dinner', np.nan, 'Dinner', 'Dinner', 'Lunch', 'Lunch', np.nan, 'Dinner', 'Dinner', 'Lunch'],
'size': [2, 4, 2, 2, 4, 2, 3, 4, 2, 2],
'table': ['table1', 'table2', 'table3', 'table4', 'table5', 'table6', 'table7', 'table8', 'table9', 'table10']}
labels= np.arange(1, 11)

df1 = pd.DataFrame(data,labels)
q6ans1 = list(df1.index)
q6ans2 = list(df1.columns)
q6ans3 = df1.dtypes
q6ans4 = df1.shape
q6ans5 = df1.head(3)
q6ans6 = df1['tip']
q6ans7 = df1[['tip']]
q6ans8 = df1.describe()
q6ans9 = df1[['day','time']].describe(include= "all")
df2 = df1.set_index('table')
q6ans11 = df2.loc['table8']
q6ans12 = df2.loc['table2':'table9']
q6ans13 = df2.iloc[1:9]
q6ans14 = df2.loc['table4']['tip']
df2['business'] = "Noodels"
df2['fraction'] = df2['tip']/df2['total_bill']
q6ans17 = df2.drop(['time', 'size'], axis = 1)
q6ans18 = df2.sort_values(by=['total_bill'],ascending=False)
q6ans19 = df2.sort_index(axis=1)
q6ans20 = df2.groupby(['day']).mean()
print(q6ans20)
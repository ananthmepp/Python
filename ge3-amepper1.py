"""
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
#Answer to Question 1
tup1=(3,1,4,1,5,9,2,5,3,6)
tup2=(7,8)*5
super_tup=tup1+tup2

print('super tuple:', super_tup)

#Answer to Question 2
mytuple = 15, 6, 11, 6, 9, 8, 18, 20, 9, 3, 11, 11, 3, 17, 0
new_mytuple=mytuple[:7]+mytuple[8:]
print('new mytuple:', new_mytuple)

#Answer to Question 3
list1=[-4,2,7,-6,3,-5,8,10,4,-10]
list2=[1,7,8,-10,2,6,-1,10,-3,-8]
cnt=0
for item in list1:
        if item in list2:
                cnt=cnt+1
print('Number of common items between list1 and list2 is:', cnt)

#Answer to Question 4
historical=3,5,1,9,0,3,9,2,4,7
predictiona=1,5,4,1,7,7,1,0,3,9
predictionb=6,0,4,3,4,4,8,4,3,7
print('')
print('historical:', historical)
print('predictiona:', predictiona)
print('predictionb:', predictionb)
print('')
for i,j,k in zip(historical, predictiona, predictionb):
        print('historical: ',i,'prediction a: ',j,'prediction b: ',k)

#Answer to Question 5
btcdec1 = [11234, 12475]
btcdec1.append(14560)
btcdec2 = [15630, 12475, 14972]
btcdec1.extend(btcdec2)
btcdec1.sort()
print(btcdec1)

#Answer to Question 6
growth_rates = [1.03, 0.9, 1.36, 1.23, 1.08, 1.12, 1.55, 1.06, 1.05, 0.92]
mult = 1
n=len(growth_rates)
for i in range(n):
    mult *= growth_rates[i]
mult = pow(mult,(1/n))
geo_mean = round(mult,2)

print('Compound annual growth rate is:',geo_mean)
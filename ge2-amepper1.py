"""
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
#Answer to Question 1
for i in range (0,27,2):
    print("Generated number", (i))

#Answer to Question 2
for i in range(3,0,-1):
    for j in range(1001,1006):
        print(str(i)+"-"+str(j))

#Answer to Question 3
input1 = int(input('Enter an integer number: '))
if input1<0:
    print("Input1 is negative")
elif input1 <= 20:
    print("Input1 is positive but 22less than or equal to 20")
else:
    print("Input1 is greater than 20")

#Answer to Question 4
j = 0
sum11 = 0

while j < 101:
    sum11 += j
    print("j:", j, "sum11:", sum11)
    j += 11

print('')
print('Total sum11 is:', sum11)

#Answer to Question 5
sum5 = 0 
sum3 = 0

i=range(1001)
for n in i:
    sum3=sum3+(3*n)
    sum5=sum5+(5*n)

print('sum3 =', sum3, 'divided by sum5 =', sum5, 'is', float(sum3)/ float(sum5))

#Answer to Question 6
from datetime import datetime, timedelta
dt = datetime(2021, 1, 26, 18, 51, 17)
dt2 = dt - timedelta(days=28)
dt2_str = dt2.strftime('%m/%d/%Y')

print('dt2_str date is:', dt2_str)

#Answer to Question 7
st=b'\xd0\x9f\xd0\xb5\xd1\x80\xd1\x83 \xd0\xbf\xd0\xbe\xd0\xb1\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82!'
russian = st.decode('utf8')
print(russian)

#Peru will win!
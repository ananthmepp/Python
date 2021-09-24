"""
@description: Answer to Part 1 of Programming Assignment 3
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
import numpy as np
import pandas as pd
def attemp_float(x):
    try:
        return float(x)
    except:
        return x

#store in data file variable
path = "./loan-data-v1.csv" # assigns file path to variable
dataFile = open(path,"rt")#assigns/stores path to variable
#dafault value is none
next(dataFile, None)

customer_list = [] #empty customer list

#for each line of data  in the data file 
for dataLine in dataFile:
    #we split the string, that is line after every comma
    tokens = dataLine.split(',') #totokenizeseach comma-separated line in your input file.
    tokens[-1] = tokens[-1].strip("\n") #tokens[-1] is the last vale, also confirms that the \n is removed so the rows are not seperated

    i=0 #initialize i
    for token in tokens:
       tokens[i] = attemp_float(tokens[i]) #convert every token in tokens too a float
       i = i+1 #adds to i as you convert more
    
    customer_list.append(tokens) #appends tokens

#length-i-1
length = len(customer_list)
for i in range(0, length): 
    for j in range(0, length-i-1):
        #7 is the index for days deliquent
        if (customer_list[j][7] < customer_list[j + 1][7]): 
            temp = customer_list[j] 
            customer_list[j]= customer_list[j + 1] 
            customer_list[j + 1]= temp
lambda_function = lambda x: x[7] >= 90 #True if Days Delinquent float value is greater than or equal to 90, otherwise, returns False
# store data in new list
customer_list2 = filter(lambda_function, customer_list)
customer_list = customer_list2
output_filename = "loan-data-output-v1.csv" #name of new output file
output_file = open(output_filename, "w")#open the new file

header_list = ['Name', 'State', 'Days Delinquent', 'Years as Customer']#headers in new excel file
header_str = ','.join(header_list)#adds commas to headers
header_str = header_str + '\n' #new row

output_file.write(header_str)

for dataLine in customer_list: #line in the customer list 
    s = ','.join([dataLine[0], dataLine[1], str(dataLine[7]), str(dataLine[10])]) #join the data with commas
    s = s + '\n' #next line 
    output_file.write(s) #write into file

dataFile.close()
output_file.close() 
"""
@description: Answer to Part 2 of Programming Assignment 3
@author: Ananth Mepperla
@email: amepper1@asu.edu
"""
import sqlite3
import pandas as pd
from pandas import DataFrame
#Establish a connection with the database. 
#Changing the code below will result in ZERO points. 
conn = sqlite3.connect('./app-db.sqlite')
df1 = pd.read_sql_query("SELECT * FROM app_info", conn)
df2 = pd.read_sql_query("SELECT * FROM app_stats", conn)
conn.close()
df3=df1.merge(df2, on = "app_name")
df3.info()
# the two data frames got merged and goto ride of redundent info
q2a1 = df3.head(5)
q2a2 = df3.describe()
q2a3 = df3.describe()

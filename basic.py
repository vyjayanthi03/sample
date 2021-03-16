"""
## TO READ CSV FILE
import pandas as pd
df = pd.read_csv("C:/Users/SSS2016056/Desktop/file1.csv")
print(df)
df.shape

df.describe()
df.values
"""
"""
#TO READ CSV FILE IN PYTHON
#(https://www.guru99.com/python-csv.html)

import csv 
with open('C:/Users/SSS2016056/Desktop/file1.csv', 'rt') as file:
    data = csv.reader(file)
    for row in data:
        print(row)

"""

import pandas as pd
music_data = pd.read_csv(r"C:\Users\SSS2016056\Desktop\music.csv")
print(music_data)


"""
class bottle:
    def __init__(self,color,type,company):
        self.color = color
        self.type = type
        self.company=company
"""

temp = 25
if temp >30:
    print("its very hot outside")
    print("drink plenty of water")
elif temp >20: #(20 ,30]
    print("ots nice day")
elif temp>10: #(10,20]
    print("its bit cold")
else:
    print("its cold")
print('done')

##########
# TO CALCULATE THE WEIGHT

wt = int(input("enter ur weight"))
unit= input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = wt/0.45
    print("weight in Lbs:"+converted)
else:
    converted =wt *0.45
    print("weight in kgs: "+str(converted))





# STRING FUNCTIONS
s = "sample text"
print(s)
print(s.lower())
print(s.upper())

print(s.find('2'))
print(s.replace('s','a'))
print('sample' in s)
print('smple' in s)













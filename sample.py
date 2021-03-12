import pandas as pd
df = pd.read_excel(r"C:/Users/SSS2016056/Desktop/ptest.xlsx")
u = df['first_refer']
i=0
for j in u:
    if i <len(u):
        print(u[i])
        i+=1



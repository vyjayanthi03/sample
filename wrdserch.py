
"""
import pandas as pd
import re
url="https://www.youtube.com/results?search_query=talend+tutorial+for+beginners"
l = re.split(r"\W+",url)
#print(l)
#df = pd.read_excel("C:/Users/SSS2016056/Desktop/Employees.xlsx")
#print(df)

names = {'keyword': l}
print(names)
df = pd.DataFrame(names, columns=['keyword'])

df.loc[(df['keyword'] == 'google') | (df['keyword'] == 'bing'), 'category'] = 'organic search'
df.loc[(df['keyword'] == 'results') | (df['keyword'] == 'youtube'), 'category'] = 'organic social'

print(df)

"""
import pandas as pd
from bs4 import BeautifulSoup
url = "https://codepen.io/features/pro"












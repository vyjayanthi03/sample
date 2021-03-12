
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# url = "https://pythonprogramming.net/beginner-python-programming-tutorials/"
# html = urlopen(url)
# soup = BeautifulSoup(html, 'lxml')
# type(soup)
# title = soup.title
# print(title)
# hyper=soup.find_all('a')
# print(hyper)


# # # page = requests.get(url) # to extract page from website
# # # html_code = page.content
# # # soup = BeautifulSoup(html_code, 'html.parser') #Parse html code
# # # texts = soup.findAll(text=True) #find all text
# # # text_from_html = ' '.join(texts) #join all text


#from pyexcel_xlsx import get_data
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url='https://www.yahoo.co.in/search?source=h+data+onAAZ0CiAGMQ4dUDCAg&uact=5'
#df = pd.read_excel(r"C:/Users/SSS2015045/Desktop/ptest.xlsx")
df = pd.read_excel(r"C:\Users\SSS2016056\Desktop\ptest.xlsx")
df_list = list(df['first_refer'])
# print(df_list[0])
# for i in df_list['first_refer']:
#
#     output = []
#     output['first_refer[1]'] = output[first_refer][0]
#     print(output)


# print(df_list)

# list1 = list(df['first_refer'])
# # for i in list
#
# # # col=df.iloc[0]
# # print(col)
# #print(df)
#
#print(df_list[0])
url = df_list[1]
#
#
keywords1 = ['facebook', 'linkedin', 'youtube']
keywords2 = ['google', 'bing', 'yahoo', 'gmail']
keywords3 = ['ads', 'amazon']

for l in df_list:

    for key in keywords1:
        if key in l:
            print('Organic Social')

    else:
        for key in keywords2:
            if key in l:
                print('Organic search')

        else:
            for key in keywords3:
                if key in l:
                    print('paid marketing')













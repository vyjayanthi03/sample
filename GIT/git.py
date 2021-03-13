# TO FIND A SPECIFIC WORD IN WEBPAGE AND COUNT IT.
"""
import requests
from bs4 import BeautifulSoup
url = input("enter the url: ")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
g = list(soup)
t = 0
for x in range (len(g)-5):

    if g[x]+g[x+1]+g[x+2]+g[x+3]+g[x+4]+g[x+5]== "  code ":
        t= t+1
    print(t)

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/URL'
the_word = 'resource'
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, 'lxml')
words = soup.find(text=lambda text: text and the_word in text)
print(words)
count = len(words)
print('\nUrl: {}\ncontains {} occurences of word: {}'.format(url, count, the_word))

"""
"""
words = ['Python', 'supports', 'orange']
site = urllib.request.urlopen(https://en.wikipedia.org/wiki/Python_(programming_language)).read()
for word in words:
    if word in site:
        print(word)
    else:
        print(word , "not found")
"""

import re
pattern = "Coookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print("match!")
else:
    print("not a match")

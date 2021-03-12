d = {1:10,2:30,3:40,5:70}
def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

"""
def word(filename,listofwrds)
    try:
        file = open
"""

import pandas as pd
lst = ['dont','give','ur','life','remote','to','others']
df = pd.DataFrame(lst)
print(df)

"""
BELOW CODE TO CHECK WHETHER TWO GIVEN WORDS PRSNT IN SPECIFIED COLUMN OF
A GIVEN DATAT FRAME

SOURCE OF CODE:https://www.w3resource.com/python-exercises/pandas/string/python-pandas-string-exercise-35.php

"""

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['9910 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)
def test_and_cond(text):
    result = re.findall(r'(?=.*Ave.)(?=.*9910).*', text)
    return " ".join(result)
df['check_two_words']=df['address'].apply(lambda x : test_and_cond(x))
print("\nPresent two words!")
print(df)












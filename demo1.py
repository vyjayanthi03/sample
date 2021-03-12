"""
def func():
    print('Hello')
func()
#using return funvction
def fun1(x):
   return x*x*x

print(fun1(2))

def cube(num):
    return num*num*num
result = cube(4)
print(result)

#IF STMNTS:
is_male = True
is_tall = False
if is_male and is_tall:
    print('you are a tall man')
elif is_male and not(is_tall):
    print('u are a short male')
elif not(is_male) and is_tall:
    print("u are not a male but u r taller")
else:
    print("u r either not male or tall or both")

"""
"""
import base64
from github import Github
from pprint import pprint

# Github username
username = "vyjayanthi03"

# pygithub object
g = Github()

#get that user by username

user = g.get_user(username)

for repo in user.get_repos():
    print(repo)
"""

def print_repo(repo):

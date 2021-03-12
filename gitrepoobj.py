
from github import Github
from git import *
token = Github("da5a5e0bd2d4581e262739aa22dfb70cc20e8f38")
user_data = token.get_user("vyjayanthi03")
user_repo = user_data.get_repo("sample")

for repo in user_data.get_repos():
    print("repo_name :", repo.name)
#    print("repo_id :", repo.id)
 #   print("repo_created_date :", repo.created_at)
  #  print("total_commits :", repo.get_commits().totalCount)
   # print("last_commit_date:", repo.updated_at)



"""
from github import Github
ACCESS_TOKEN = "da5a5e0bd2d4581e262739aa22dfb70cc20e8f38"
g = Github(ACCESS_TOKEN)
print(g.get_user().get_repos())

import requests
from pprint import pprint

username = "vyjayanthi03"
url = f"https://api.github.com/users/{username}"
user_data = g.get(requestsurl).json()

pprint(user_data)
"""












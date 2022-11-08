import requests
import json
from config import apiKey
from github import Github

# Api key stored in config file
g = Github(apiKey)

#retrieve all files in my data representation coursework repository
repo = g.get_repo("MegTully/data-representation-coursework")
#print url to repository to check it
print(repo.clone_url)


Contents = repo.get_contents("assignment03-cso.py")
FileUrl = Contents.download_url
print (FileUrl)

response = requests.get(FileUrl)
contentOfFile = response.text
print (contentOfFile)



#filename= "Github_Repositories.json"


#url = "https://api.github.com/repos/MegTully/data-representation-coursework/contents"

#response = requests.get(url, auth = ('token', apiKey))
#print(response.status_code)

#repoJSON=response.json()

#with open (filename, 'w') as fp:
#    json.dump(repoJSON, fp , indent = 4)

# replace all instances of 'r' (old) with 'e' (new)
#new_string = string.replace("r", "e" )
 
#print(string)
#print(new_string)

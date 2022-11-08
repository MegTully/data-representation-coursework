import requests
import json
from config import apiKey
from github import Github

#File to be edited as a variable so file can be changed 
RepositoryFile = "Text.json"
# Api key stored in config file
g = Github(apiKey)

#retrieve all files in my data representation coursework repository
repo = g.get_repo("MegTully/data-representation-coursework")
#print url to repository to check it
print(repo.clone_url)

#I added a json file to my repo that had the name Andrew in it so that I could see if this prog worked
#Contents is a variable that stores all the info from inside the Text.json file
Contents = repo.get_contents(RepositoryFile)
#Create a variable to store the url to the contents inside .json file
FileUrl = Contents.download_url
print (FileUrl)

#Our download URL is used to make a http request to the .json file 
response = requests.get(FileUrl)
#output the contents of the file
contentOfFile = response.text
print (contentOfFile)

#Overwrite the contents in the file by changing any string with value andrew to a new string called Megan
newContents = contentOfFile.replace("Andrew","Megan")
print (newContents)

#Update the file inside the github repo 
gitHubResponse=repo.update_file(Contents.path,"Changed all instances of Andrew to Megan",
newContents,Contents.sha)
print (gitHubResponse)



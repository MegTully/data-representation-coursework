#Import necessary packages
import requests
import csv
from xml.dom.minidom import parseString
#Irish rail train times from website
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#Array for for loop below 
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]
  
#create a csv file called train.csv and is referred to as train_file
with open('train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#get elements inside objTrainPositions tag
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    #for loop that assigns all the traincodes(inside TrainCode tag) to variable traincode
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        
    #create an empty array called datalist to add train info to
        dataList = []
        #if statement only runs for loop if traincode begins wit "D"
        if traincode.startswith("D"):
            #gets all the info under the headings in the retrieveTag array at top of page
            #adds all the info to datalist and then datalist is printed to csv file created above
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
                train_writer.writerow(dataList)
                dataList.append(traincode)
                train_writer.writerow(dataList)

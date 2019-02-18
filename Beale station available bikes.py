"""
Created on Sun Feb 2019

@author: Liza Chaplygina

This code shows the number of bikes/ebikes available at the closest
to my home station, docks available at the closest to the school station 
and vice versa

"""


import urllib.request # instead of urllib2 like in Python 2.7
import json


##################
# Defining the function that will print out the number of bikes and docks
##################

def printResults(data):
  # loading the string data into a dictionary
  theJSON = json.loads(data)
  # content of JSON is read as a Python object
  
  x=0 # index of a station we are looking for
  y=0
  
  # index for the "home" bike station at Beale
  
  for i in theJSON["data"]["stations"]:
    if i['station_id'] == "27": 
      global index1
      index1 = x
    else:
      x = x + 1
 
  
  # index for the "school" bike station at Beale
  
  for i in theJSON["data"]["stations"]:
    if i['station_id'] == "6":
      global index2
      index2 = y
    else:
      y = y + 1
  
# NUMBER of bikes/docks available

  my_answer = input('Are you going to school or home? (enter: school/home)\n\nYour answer: ').lower()
  if 'school' in my_answer:
     print ('\n***********************************')
     print ('\nBeale st:', theJSON['data']['stations'][index1]['num_bikes_available'], 'bikes (', theJSON['data']['stations'][index1]['num_ebikes_available'], 'ebikes)','available')
     print ('Embarcadero at Sansome:', theJSON['data']['stations'][index2]['num_docks_available'], 'docks available')
     print ('\n***********************************')
  elif 'home' in my_answer:
    print ('\n***********************************')
    print ('\nEmbarcadero at Sansome:', theJSON['data']['stations'][index2]['num_bikes_available'], 'bikes (', theJSON['data']['stations'][index2]['num_ebikes_available'], 'ebikes)','available')
    print ('Beale st:', theJSON['data']['stations'][index1]['num_docks_available'], 'docks available')
    print ('\n***********************************')
  
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the data from the fordgo bike station status json file

  urlData = "https://gbfs.fordgobike.com/gbfs/fr/station_status.json"
  
  # Open the URL and read the data
  
  webUrl = urllib.request.urlopen(urlData)
  
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
  main()
  
  
  

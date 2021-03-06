import json
import re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def getCleanCorpusEnglish():
    with open('./training/services_en.json') as file: 
        data = json.load(file)

    # print("Service ID: "+data[0]["id"])
    # print("Service Name: "+data[0]["name"])   
    #data[i]["name"] +" ," + data[0]["description"]+" ," + data[i]["output"]+" ," + data[i]["service_fees"] +" ," + data[i]["faqs"]
    i = 0
    result = ""
    count = len(data)
    print("Count=",count)
    while i < count:
        result += data[i]["name"] +"," + data[i]["description"]+"," + data[i]["output"]+"," + data[i]["service_fees"] +"," + data[i]["faqs"]
        i+=1
    
    clean_result = cleanhtml(result)
    strippedText = str(clean_result).replace('[','').replace(']','').replace('\'','').replace('\"','').replace('(','').replace(')','').replace('/','')
    return strippedText


import json


def getcleanCorpusEnglish():
    with open('./training/services_en.json') as file: 
        data = json.load(file)

    # print("Service ID: "+data[0]["id"])
    # print("Service Name: "+data[0]["name"])   
    #data[i]["name"] +" ," + data[0]["description"]+" ," + data[i]["output"]+" ," + data[i]["service_fees"] +" ," + data[i]["faqs"]
    i = 0
    result = ""
    count = len(data)
    print("All Services Count="+count)
    while i < count:
        result += data[i]["name"] +"," + data[i]["description"]+"," + data[i]["output"]+"," + data[i]["service_fees"] +"," + data[i]["faqs"]
        i+=1
    #print(data["name"] +" ," + data["description"]+" ," + data["output"]+" ," + data["service_fees"] +" ," + data["faqs"])
    return result


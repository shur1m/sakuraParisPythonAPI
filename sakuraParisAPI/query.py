import requests
import json
import re
from entryClass import Entry

# return [[Entry], nextPageMarker]
def queryApi(word : str, dictionary : str, maxEntries = 40, type = 1, romaji = 0, marker = "", removeTags = True):
    url = "https://sakura-paris.org/dict/"
    params = {
        "api" : "1",
    }

    params["q"] = word
    params["dict"] = dictionary
    params["type"] = str(type)
    params["romaji"] = romaji
    params["max"] = min(maxEntries, 40)
    
    if marker != "":
        params["marker"] = marker

    result = None

    #try getting the api response and parse
    try:
        response = requests.get(url, params)

        #if response was received, parse and place in result
        if response:
            responseObj = response.json()

            if isinstance(responseObj, list):
                result = [convertToEntryList(responseObj), ""]


            elif isinstance(responseObj, object):
                result = [convertToEntryList(responseObj["words"]), responseObj["nextPageMarker"]]

            

        #if no response do nothing 


    except Exception as e :
        print("---EXCEPTION OCCURRED IN FUNCTION sakuraParisAPI.getEntries---")
        print(e)

    return result

#converts list of dictionaries into list of entries
def convertToEntryList(dicList: list[Entry]):
    result = []

    for word in dicList:
        heading = word["heading"]
        text = word["text"]
        page = ""
        offset = ""

        if "page" in word:
            page = word["page"]

        if "offset" in word:
            offset = word["offset"]

        result.append(Entry(heading, text, page, offset))

    return result

#returns output without tags
def removeTags(input: str):
    return re.sub(r'\[.*?\]', '', input)

a = queryApi("か", "広辞苑", 10)[0]

for entry in a :
    print(entry.getHeading())
    print(entry.getDefinition())

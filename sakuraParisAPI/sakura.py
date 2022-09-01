#This file holds Sakura, which is the main port to the API
from sakuraParisAPI.fetch import query

class JpDict:
    def __init__(self, maxEntries = 10, dictionaries = {"広辞苑"}):
        self._maxEntries = maxEntries
        self._dictionaries = dictionaries
        self._removeTags = True
        self._allDicts = set(query.getAllDict())

    #returns a dictionary [key = dict name, value = list of Entry]
    def search(self, word, searchType = 0):
        result = {}

        for dictionary in self._dictionaries:
            result[dictionary] = []
            self._addEntries(result[dictionary], dictionary, word, searchType)

        return result

    def _addEntries(self, curList, dictionary, word, searchType):
        remaining = self._maxEntries
        queryResult = query.askApi(word, dictionary,
            removeTags = self._removeTags,
            type = searchType,
            maxEntries = min(remaining, 40))

        curList.extend(queryResult[0])
        remaining -= len(queryResult[0])

        while remaining > 0 and queryResult[1] != "":
            queryResult = query.askApi(word, dictionary,
                removeTags = self._removeTags,
                type = searchType,
                marker = queryResult[1],
                maxEntries = min(remaining, 40))
            
            curList.extend(queryResult[0])
            remaining -= len(queryResult[0])
    
    #same as default search
    def startsWith(self, word):
        return self.search(word)

    #searches for words that end with word
    def endsWith(self, word):
        return self.search(word, searchType = 1)

    #searches for complete matches
    def completeMatch(self, word):
        return self.search(word, searchType = 2)

    #sets max number of entries returned for each search
    def setMax(self, maxEntries):
        if maxEntries >= 1:
            self._maxEntries = maxEntries

    #adds dictionary to list of dictionaries to be searched
    def addDict(self, dictionaryName):
        if dictionaryName in self._allDicts:
            self._dictionaries.add(dictionaryName)

    #adds all possible dictionaries to active dictionaries
    def addAllDict(self):
        self._dictionaries.update(self.getAllDict())

    #removes dictionary from dictionaries to be searched
    def removeDict(self, dictionaryName):
        if dictionaryName in self._dictionaries:
            self._dictionaries.remove(dictionaryName)

    #disables all dictionaries
    def clearDict(self):
        self._dictionaries.clear()

    #returns all active dictionaries as a list
    def getDict(self):
        return list(self._dictionaries)

    #return all possible dictionaries
    def getAllDict(self):
        return self._allDicts

    #leaves markdown tags in output
    def enableTags(self):
        self._removeTags = False

    #removes markdown tags from output
    def disableTags(self):
        self._removeTags = True

    
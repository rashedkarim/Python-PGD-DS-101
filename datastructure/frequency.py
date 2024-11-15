
def characterFrequency(sourceText, myList):
    myDict = dict()
    for x in sourceText.replace(',', '').replace('.', ''):
        if x in myList:
            if x in myDict.keys():
                myDict[x] = myDict[x] + 1
            else:
                myDict[x] = 1
    return myDict

def wordFrequency(sourceText, myList):
    myDict = dict()
    for x in sourceText.replace(',', '').replace('.', '').split(" "):
        if x in myList:
            if x in myDict.keys():
                myDict[x] = myDict[x] + 1
            else:
                myDict[x] = 1
    return myDict
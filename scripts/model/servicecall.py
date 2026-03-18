import json

class ServiceCall(object):

    def __init__(self, fields, data):
        index = 0
        self.dataDict = {}
        for field in fields:
            if len(data[index].strip()) > 0:
                # data exists
                #print(self.dataDict)
                self.dataDict[field] = data[index].strip()
            index += 1
        #print(self.dataDict)

    def toJson(self):
        return json.dumps(self.dataDict, indent=4)
    
    def dataDict(self):
        return self.dataDict

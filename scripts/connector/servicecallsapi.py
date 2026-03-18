
from http.client import HTTPConnection
import pprint
import json
from model.servicecall import ServiceCall
import requests

class ServiceCallsApi(object):

    ipAddress = 'localhost'
    port = 80
    
    def __init__(self, ipAddress='localhost', port=8080):
        self.ipAddress = ipAddress
        self.port = port
        self.url = 'http://'+ipAddress+':'+str(port)
        
    def createServiceCall(self, body):
        headers = {"Content-type": "application/json"}
        #,
        #"Accept": "text/plain"}
        r = requests.post(self.url+'/servicecalls', data=body, headers=headers)
        if(r.status_code not in [requests.codes.ok, requests.codes.created]):
            print(r.__dict__)
            print("failed create operation: "+str(r.status_code))
            print("message: "+str(r.text))
            r.raise_for_status()
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(r)
        #pp.pprint(r.headers)
        #pp.pprint(r.text)
        pp.pprint(r.json())

    def updateServiceCall(self, cadNumber, body):
        headers = {"Content-type": "application/json"}
        r = requests.put(self.url+'/servicecalls/'+str(cadNumber), data=body, headers=headers)
        if(r.status_code not in [requests.codes.ok, requests.codes.created]):
            print("failed update operation: "+str(r.status_code))
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(r)
        #pp.pprint(r.headers)
        #pp.pprint(r.text)
        pp.pprint(r.json())
        
    def deleteServiceCall(self, serviceCall):
        r = requests.delete(self.url+'/servicecalls/'+str(serviceCall.getRowId()))
        if(r.status_code is not requests.codes.ok):
            print("failed delete operation: "+str(r.status_code))
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(r.headers)
        
    def getServiceCall(self, serviceCall):
        r = requests.get(self.url+'/servicecalls/'+str(serviceCall.getRowId()))
        if(r.status_code is not requests.codes.ok):
            print("failed get operation: "+str(r.status_code))

        dataJson = r.json()
        
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(r.headers)
        #pp.pprint(dataJson)
        
        return dataJson
    
    def getAll(self):
        r = requests.get(self.url+'/servicecalls')
        if(r.status_code is not requests.codes.ok):
            print("failed getAll operation: "+str(r.status_code))

        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint("Headers: {}".format(r.headers))
        #print(r.encoding)
        #print(r.text)
        #print(type(r.json()))
        #pp.pprint("Json: {}".format(r.json()))

        dataJson = r.json()
        serviceCalls = []
        #print("serviceCalls count:", len(serviceCalls))
        if(len(dataJson)) > 0:
            for item in dataJson:
                #print("Item type:", type(item))
                #print("Item:", item)
                serviceCall = ServiceCall().fromJsonDict(item)
                serviceCalls.append(serviceCall)
        return serviceCalls

    
    ##### Realtime versions #######
    def createServiceCallRealtime(self, body):
        headers = {"Content-type": "application/json"}
        #,
        #"Accept": "text/plain"}
        r = requests.post(self.url+'/servicecalls/realtime', data=body, headers=headers)
        # print(r.status_code)
        if(r.status_code is not requests.codes.ok):
            #print(r.__dict__)
            print("failed create operation: "+str(r.status_code))
            r.raise_for_status()

        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(r.headers)
        #pp.pprint(r.text)
        #pp.pprint(r.json())


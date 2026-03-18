#!/usr/bin/python

import sys
import getopt
import time
import csv
import pprint

from model.servicecall import ServiceCall
from connector.servicecallsapi import ServiceCallsApi

from csvfieldcreator import fieldNames

def loadData(inputFile, maxCount):

    fields = fieldNames(inputFile)
    
    conn = ServiceCallsApi()
    with open(inputFile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  # Reader object

        next(csvreader)  # Read header and skip it

        index = 1
        for row in csvreader:
            serviceCall = ServiceCall(fields, row)
            jsonData = serviceCall.toJson()
            index += 1
            conn.createServiceCall(jsonData)
            if index > maxCount:
                break

def main(argv):
    inputFile = ''
    outputFile = ''
    maxCount = 100
    try:
        opts, args = getopt.getopt(argv,"hi:o:c:",["ifile=","ofile=","count"])
    except getopt.GetoptError:
        print ('incidentreportload.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    if len(opts) < 1:
        print ('incidentreportload.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
           
    for opt, arg in opts:
        if opt == '-h':
            print ('incidentreportslooad.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-c", "--count"):
            maxCount = int(arg)

    print ('Input file is "', inputFile)
    print ('Output file is "', outputFile)
    loadData(inputFile, maxCount)

    
if __name__ == "__main__":
    print ('python.vesion', sys.version)
    main(sys.argv[1:])




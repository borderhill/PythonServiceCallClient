#!/usr/bin/python

import sys
import getopt
import time
import csv
import pprint

from model.servicecall import ServiceCall
from connector.servicecallsapi import ServiceCallsApi

def fieldNames(inputFile):
    cFields = []
    with open(inputFile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  # Reader object

        fields = next(csvreader)  # Read header

        time.sleep(1)
        for field in fields:
            if '_' in field:
                parts = field.split('_')
                # Capitalize each word after the first and join them back together
                res = parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])
                cFields.append(res)
            elif ' ' in field:
                parts = field.split(' ')
                # Capitalize each word after the first and join them back together
                res = parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])
                cFields.append(res)
            else:
                # make lower case
                res = field.lower()
                cFields.append(res)
    print("FIELDS : ",cFields)
    return cFields

# -i /Users/arirajamaki/Work/Python/SFPD-ServiceCallsClient/data/Law_Enforcement_Dispatched_Calls_for_Service__Closed_20260302.csv
# -i /Users/arirajamaki/Work/Python/SFPD-ServiceCallsClient/data/Law_Enforcement_Dispatched_Calls_for_Service__Real-Time_20260302.csv
# -i /Users/arirajamaki/Work/Python/SFPD-ServiceCallsClient/data/Police_Department_Incident_Reports__2018_to_Present_20260302.csv
def main(argv):
    inputFile = ''
    outputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('csvfieldcreator.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    if len(opts) < 1:
        print('csvfieldcreator.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
           
    for opt, arg in opts:
        if opt == '-h':
            print('csvfieldcreator.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg

    print('Input file is "', inputFile)
    print('Output file is "', outputFile)
    fields = fieldNames(inputFile)
    
if __name__ == "__main__":
    print('python.vesion', sys.version)
    main(sys.argv[1:])




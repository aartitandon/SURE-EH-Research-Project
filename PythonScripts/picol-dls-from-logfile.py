#!/usr/bin/python3

###########################################################
# a python program to connect to a json file of the logs
# from the PLN-Info Firestore DB and count the downloads
# by product name, epa reg and for the H&S translations
# display page 
# output is roughly csv with a header row
###########################################################
# 1. Accept 1 argument on the command line: the name of the
#    JSON file
# 2. write output directly to the console 

import json, operator, io
import sys

def countPICOLDls(logs):
    dls = {}
    for log in logs:
        if (log['evType'] == 'evDownloadLabel') and (log['evDesc3'] == 'PICOL'):
            nameReg = log['evDesc2'] + ' | ' + log['evDesc1']
            if nameReg not in dls:
                dls[nameReg] = 0
            dls[nameReg] += 1
    print('"NameReg", "Count"')
    for dl in sorted(dls) :
        print('"{0}", {1}'.format(dl, dls[dl]))

def load_input(inFname):
    with io.open(inFname, 'r', encoding='utf-8') as json_file:  
        logs = json.load(json_file)
    return logs

def printhelp():
    print(sys.argv[0], 'input filename')
    print('eg: ', sys.argv[0], '2020.json')
    return

def main():
    # test for number of arguments
    if len(sys.argv) != 2:
        printhelp()
        sys.exit(2)
    input_filename = sys.argv[1]

    logs = load_input(input_filename)
    countPICOLDls(logs)

    sys.exit(0)


main()

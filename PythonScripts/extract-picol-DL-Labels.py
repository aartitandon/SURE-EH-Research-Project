#!/usr/bin/python3

###########################################################
# 1 a python program to grab the download records from a
#   file of all log records in JSON format.
# 2 ignores aids in the ignores.csv file
# 3 output is in CSV format
# 4 output is written to stdout
# 5 input filename is required on the command line
# 6 input file must be json formatted
###########################################################
# TODO

import json, operator, io
import sys
import csv

def countPICOLDls(logs, ignores):
    dls = {}
    for log in logs:
        if (log['aid'] not in ignores) and (log['evType'] == 'evDownloadLabel') and (log['evDesc3'] == 'PICOL'):
            nameReg = log['evDesc2'] + ' | ' + log['evDesc1']
            if nameReg not in dls:
                dls[nameReg] = 0
            dls[nameReg] += 1
    print('"NameReg", "Count"')
    for dl in sorted(dls) :
        print('"{0}", {1}'.format(dl, dls[dl]))

def load_ignores(ignoreFname):
    ignores = []
    with io.open(ignoreFname, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ignores.append(row['aid'])
    return ignores

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
    ignores = load_ignores('ignores.csv')
    logs = load_input(input_filename)
    countPICOLDls(logs, ignores)

    sys.exit(0)

main()
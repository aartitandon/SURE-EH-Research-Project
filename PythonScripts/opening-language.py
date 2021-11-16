#!/usr/bin/python3

###########################################################
# a python program to connect to a json file of the logs
# from the PLN-Info Firestore DB and count:
# 0. ignore the devices in the ignores.csv file
# 1. opening language counts 
# 2. ios vs android
#
# output is roughly csv with a header row
###########################################################
# 1. Accept 1 argument on the command line: the name of the
#    JSON file
# 2. write output directly to the console 

import json, operator, io, csv
import sys

def load_ignores(ignoreFname):
    ignores = []
    with io.open(ignoreFname, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ignores.append(row['aid'])
    return ignores

def countOS(logs, ignores):
    devs = {}
    andCount = 0
    andEnCount = 0
    andEsCount = 0
    iosCount = 0
    iosEnCount = 0
    iosEsCount = 0
    totCount = 0
    totEsCount = 0
    totEnCount = 0

    checkNext = False
    iosFlag = False
    andFlag = False

    for log in logs:
        if (log['evType'] == 'evStart'):
            checkNext = True
            dev = log['aid']
            if dev not in ignores:
                totCount += 1
                s: string = log['evDesc2']
                if s.find('ios') > -1:
                    iosCount += 1
                    iosFlag = True
                if s.find('android') > -1:
                    andCount += 1
                    andFlag = True
        elif ((checkNext) and (log['evType'] == 'evViewPage') and (log['evDesc1'] == 'Labels Search')):
            checkNext = False
            lg = log['evDesc2']
            if iosFlag:
                if lg == 'es':
                    iosEsCount += 1
                else:
                    iosEnCount += 1
            if andFlag:
                if lg == 'es':
                    andEsCount += 1
                else:
                    andEnCount += 1
            iosFlag = False
            andFlag = False

    totEsCount = andEsCount + iosEsCount
    totEnCount = andEnCount + iosEnCount

    print('"OS", "Count", "En Count", "Es Count"')
    print('"iOS", {0}, {1}, {2}'.format(iosCount, iosEnCount, iosEsCount))
    print('"android", {0}, {1}, {2}'.format(andCount, andEnCount, andEsCount))
    print('"total", {0}, {1}, {2}'.format(totCount, totEnCount, totEsCount))

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
    ignores = load_ignores('ignores.csv')
    countOS(logs, ignores)

    sys.exit(0)


main()

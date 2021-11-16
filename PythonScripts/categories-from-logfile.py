#!/usr/bin/python3

###########################################################
# a python program to connect to a json file of the logs
# from the PLN-Info Firestore DB and count the categories
# opened from the H&S translations display page 
# output is roughly csv with a header row
###########################################################
# 1. Accept 1 argument on the command line: the name of the
#    JSON file
# 2. write output directly to the console 

import json, operator, io
import sys

def srtFn(e):
    return e[e]

def countCategories(logs):
    cats = {}
    for log in logs:
        if (log['evType'] == 'evCategoryOpen'):
            category = log['evDesc3']
            if category not in cats:
                cats[category] = 0
            cats[category] += 1

    srtd = dict(sorted(cats.items(), key=lambda x:x[1], reverse=True))
    print('"Category", "Count"')
    sum = 0
    for cat in srtd:
        pos = cat.find('Category: ')
        cat2 = cat[(pos + 10):]
        print('"{0}",{1}'.format(cat2, srtd[cat]))
        sum += srtd[cat]

    print('"Total", {0}'.format(sum))

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
    countCategories(logs)

    sys.exit(0)


main()

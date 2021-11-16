#!/usr/bin/python3

###########################################################
# a python program to connect to a json file of the logs
# from the PLN-Info Firestore DB and count:
# 0. ignore the devices in the ignores.csv file
# 1. total number of devices conncected 
# 2. for each device, the number of times the app started
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

def countDevices(logs, ignores):
    devs = {}
    for log in logs:
        if (log['evType'] == 'evStart'):
            dev = log['aid']
            if dev not in ignores:
                if dev not in devs:
                    devs[dev] = 0
                devs[dev] += 1

    srtd = dict(sorted(devs.items(), key=lambda x:x[1], reverse=True))
    print('"Device", "Count"')
    tot = 0
    cnt = 0
    for dev in srtd:
        print('"{0}",{1}'.format(dev, srtd[dev]))
        tot += srtd[dev]
        cnt += 1
    print('"Total uses", {0}'.format(tot))
    print('"Unique Devices", {0}'.format(cnt))
    if cnt > 0:
        print('"Mean uses per device", {0:0.3f}'.format(tot/cnt))

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
    countDevices(logs, ignores)

    sys.exit(0)


main()

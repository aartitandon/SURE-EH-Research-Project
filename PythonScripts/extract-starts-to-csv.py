#!/usr/bin/python3

###########################################################
# a python program to connect to a json file of the logs
# from the PLN-Info Firestore DB and create an output file
# in CSV format from the records where evType = 'evStart'. 
# This filters out records from devices listed in the 
# ignores.csv file
###########################################################
# Note: this ONLY works with non-nested JSON
###########################################################
# 1. Accept 1 argument on the command line: the name of the
#    JSON file
# 2. write output destructively to a file with the same
#    name suffixed with '-start.csv'
###########################################################

import json, operator, io, csv
import sys, os

def json2csv(infname, outfname, ignores):
    indata = load_input(infname)
    outfile = open(outfname, 'w')
    csvwriter = csv.writer(outfile)
    hdrwritten = False
    for rec in indata:
        if not hdrwritten:
            header = rec.keys()
            csvwriter.writerow(header)
            hdrwritten = True
        dev = rec['aid']
        typ = rec['evType']
        if dev not in ignores and typ == 'evStart':
            csvwriter.writerow(rec.values())
    outfile.close()
    print('  output written to {0}'.format(outfname))

def genOutFileName(infname):
    return os.path.splitext(infname)[0] + '-start.csv'

def load_input(inFname):
    with io.open(inFname, 'r', encoding='utf-8') as json_file:  
        logs = json.load(json_file)
    return logs

def printhelp():
    print(sys.argv[0], 'input filename')
    print('eg: ', sys.argv[0], '2020.json')
    return

def loadIgnores(fname):
    ignores = []
    with io.open(fname, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ignores.append(row['aid'])
    return ignores

def main():
    # test for number of arguments
    if len(sys.argv) != 2:
        printhelp()
        sys.exit(2)
    input_filename = sys.argv[1]
    output_filename = genOutFileName(input_filename)
    print('{0} ==> {1}'.format(input_filename, output_filename))
    ignores = loadIgnores('ignores.csv')
    json2csv(input_filename, output_filename, ignores)

    sys.exit(0)


main()

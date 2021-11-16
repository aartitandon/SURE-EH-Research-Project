#!/usr/bin/python3

###########################################################
# a python program to connect to the PLN-Info Firestore DB and
# extract a range of log data 
###########################################################
# 1. Accept 2 arguments on the command line 
#    a. inclusive begin date in format YYYY-MM-DD
#    b. inclusive end date in format YYYY-MM-DD
# 2. Verify that a <= b (or swap?)
# 3. set the name of the output file to a_b.json
# 4. set a to a + 'T00:00:00.000Z'
# 5. set b to b + 'T23:59:59.999Z'
# 6. use a, b to bound the retrieval from Firestore
# 7. write directly to the specified output file 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json, operator, io
import sys

def initDB():
    # use a service account
    cred = credentials.Certificate('../pln-info-firebase-adminsdk-xyi7c-e68729a9f4.json')
    firebase_admin.initialize_app(cred)

def extract2JSON(d1, d2, fname):
    db = firestore.client()
    logs_ref = db.collection(u'logs').where(u'ts', u'>=', d1).where(u'ts', u'<=', d2 + u'T23:59:59.999Z')
    docs = logs_ref.stream()

    docsout = []
    for doc in docs:
        docsout.append(doc.to_dict())

    # get json array to write to file
    json_str = json.dumps(docsout, indent=4, sort_keys=True)

    # write file out
    with open(fname, 'w') as outfile:
        outfile.write(json_str)

    #print(json.dumps(docsout, indent=4, sort_keys=True))
    #print(json.dumps(docsout, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8'))

def checkdate(dstr):
    if len(dstr) != 10:
        print(dstr, 'is not a valid date of the form YYYY-MM-DD')
        return False
    
    yr = dstr[0:3]
    sep1 = dstr[4]
    mo = dstr[5:6]
    sep2 = dstr[7]
    dy = dstr[8:9]
    if yr.isdigit() and mo.isdigit() and dy.isdigit() and sep1 == '-' and sep2 == '-':
        # print(dstr, 'passed initial tests')
        return True

    print(dstr, 'is not a valid date of the form YYYY-MM-DD')
    return False

def printhelp():
    print(sys.argv[0], 'begindate enddate')
    print('eg: ', sys.argv[0], '2020-09-30 2020-10-02')
    return

def swapvars(a, b):
    a, b = b, a
    return a, b

# print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

# test for number of arguments
if len(sys.argv) != 3:
    printhelp()
    sys.exit(2)

d1 = sys.argv[1]
d2 = sys.argv[2]

if checkdate(d1) and checkdate(d2):
    # print('date args check out')
    # swap if d1 > d2
    if d1 > d2:
        d2, d1 = d1, d2
    print('d1: ', d1, '; d2: ', d2)
    outname = d1 + u'_' + d2 + u'.json'
    initDB()
    extract2JSON(d1, d2, outname)
    sys.exit(0)

# if got to here, something wrong ==> show syntax
printhelp()
sys.exit(2)


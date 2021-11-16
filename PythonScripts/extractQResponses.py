#!/usr/bin/python3

###########################################################
# a python program to connect to the PLN-Info Firestore DB and
# extract all in app questionnaire responses, ignoring any
# responses from devices with an aid in the ignores.csv
# file
###########################################################
# 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json, operator, io
import sys
import csv

def initDB():
    # use a service account
    cred = credentials.Certificate('../pln-info-firebase-adminsdk-xyi7c-e68729a9f4.json')
    firebase_admin.initialize_app(cred)

def extract2CSV(fname, ignores):
    db = firestore.client()
    qresp_ref = db.collection(u'qanswers').order_by(u'ts', direction=firestore.Query.ASCENDING)
    docs = qresp_ref.stream()
    
    totalRecs = 0
    outRecs = 0
    ignoredRecs = 0
    docsout = []
    for doc in docs:
        docsout.append(doc.to_dict())

    outfname = fname + u'.csv'
    with open(outfname, 'w') as csvfile:
        fieldNames = ['aid', 'appver', 'lg', 'qanswer', 'qno', 'ts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames, dialect='excel')
        writer.writeheader()
        for dict in docsout:
            totalRecs += 1
            if dict['aid'] not in ignores:
                outRecs += 1
                writer.writerow({'aid': dict['aid'], 'appver': dict['appver'], 'lg': dict['lg'], 'qanswer': dict['qanswer'], 'qno': dict['qno'], 'ts': dict['ts']})
            else:
                ignoredRecs += 1

    print('Output file:        {0}'.format(outfname))
    print('total responses:    {0:4d}'.format(totalRecs))
    print('ignored responses:  {0:4d}'.format(ignoredRecs))
    print('output responses:   {0:4d}'.format(outRecs))

def load_ignores(ignoreFname):
    ignores = []
    with io.open(ignoreFname, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ignores.append(row['aid'])
    return ignores

outname = u'qAnswers'
initDB()
ignores = load_ignores('ignores.csv')
extract2CSV(outname, ignores)
sys.exit(0)



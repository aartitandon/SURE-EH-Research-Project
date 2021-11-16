#!/usr/bin/python3

###########################################################
# a python program to connect to the PLN-Info Firestore DB and
# extract label download information of app usage
###########################################################
# TODO

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

def extract2CSV(fname):
    db = firestore.client()
    logs_ref = db.collection(u'logs').where(u'evType', u'==', u'evDownloadLabel').where(u'ts', u'>=', u'2020-08-26').order_by(
    u'ts', direction=firestore.Query.ASCENDING)
    docs = logs_ref.stream()

    docsout = []
    for doc in docs:
        docsout.append(doc.to_dict())

    outfname = fname + u'.csv'
    with open(outfname, 'w') as csvfile:
        fieldNames = ['aid', 'evDesc1', 'evDesc2', 'evDesc3', 'evType', 'ts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames, dialect='excel')
        writer.writeheader()
        for dict in docsout:
            writer.writerow({'aid': dict['aid'], 'evDesc1': dict['evDesc1'], 'evDesc2': dict['evDesc2'], 'evDesc3': dict['evDesc3'], 'evType': dict['evType'], 'ts': dict['ts']})

    print('Output file: ' + outfname)

outname = u'evDownload'
initDB()
extract2CSV(outname)
sys.exit(0)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:38:56 2019

@author: root
"""

import json
from dbfread import DBF
#import dbfread
#import git

with open('/Users/alessandrodebonistrapella/Desktop/webapp consorzio/webmap_ver2/data/monitoraggio_latina_1.js', 'r+') as dataFile:
    data = dataFile.read()
    obj = data[data.find('{') : data.rfind('}')+1]
    jsonObj = json.loads(obj)
    dataFile.close() 

#for record in DBF('/Users/alessandrodebonistrapella/Google Drive/GIS DataBase/Monitoraggio/monitoraggio_latina.dbf'):
#    
#    print(record)


#with DBF('/Users/alessandrodebonistrapella/Google Drive/GIS DataBase/Monitoraggio/monitoraggio_latina.dbf') as valori_stazioni:
#    staz_si02 = valori_stazioni[0]
#    staz_si03 = valori_stazioni[1]
#    staz_si04 = valori_stazioni[2]
#    staz_si05 = valori_stazioni[3]
#    staz_si06 = valori_stazioni[4]
#    staz_sin08 = valori_stazioni[5]
#    staz_sin09 = valori_stazioni[6]
#    staz_sin10 = valori_stazioni[7]
#    staz_sin11 = valori_stazioni[8]
#    staz_sin12 = valori_stazioni[9]
#    
#    staz_si02 = dict(staz_si02)
#    staz_si03 = dict(staz_si03)
#    staz_si04 = dict(staz_si04)
#    staz_si05 = dict(staz_si05)
#    staz_si06 = dict(staz_si06)
#    staz_sin08 = dict(staz_sin08)
#    staz_sin09 = dict(staz_sin09)
#    staz_sin10 = dict(staz_sin10)
#    staz_sin11 = dict(staz_sin11)
#    staz_sin12 = dict(staz_sin12)
#    
#valori_stazioni = DBF('/Users/alessandrodebonistrapella/Google Drive/GIS DataBase/Monitoraggio/monitoraggio_latina.dbf',load=True)  

valori_stazioni = list(DBF('/Users/alessandrodebonistrapella/Google Drive/GIS DataBase/Monitoraggio/monitoraggio_latina.dbf',load=True))  


staz_si02 = valori_stazioni[0]
staz_si03 = valori_stazioni[1]
staz_si04 = valori_stazioni[2]
staz_si05 = valori_stazioni[3]
staz_si06 = valori_stazioni[4]
staz_sin08 = valori_stazioni[5]
staz_sin09 = valori_stazioni[6]
staz_sin10 = valori_stazioni[7]
staz_sin11 = valori_stazioni[8]
staz_sin12 = valori_stazioni[9]

staz_si02 = dict(staz_si02)
staz_si03 = dict(staz_si03)
staz_si04 = dict(staz_si04)
staz_si05 = dict(staz_si05)
staz_si06 = dict(staz_si06)
staz_sin08 = dict(staz_sin08)
staz_sin09 = dict(staz_sin09)
staz_sin10 = dict(staz_sin10)
staz_sin11 = dict(staz_sin11)
staz_sin12 = dict(staz_sin12)


jsonObj['features'][0]['properties'] = staz_si02
jsonObj['features'][1]['properties'] = staz_si03
jsonObj['features'][2]['properties'] = staz_si04
jsonObj['features'][3]['properties'] = staz_si05
jsonObj['features'][4]['properties'] = staz_si06
jsonObj['features'][5]['properties'] = staz_sin08
jsonObj['features'][6]['properties'] = staz_sin09
jsonObj['features'][7]['properties'] = staz_sin10
jsonObj['features'][8]['properties'] = staz_sin11
jsonObj['features'][9]['properties'] = staz_sin12


    
prova = str(jsonObj)

prova = prova.replace("'",'"')

f= open("/Users/alessandrodebonistrapella/Documents/alessandrodebonistrapella.github.io/data/monitoraggio_latina_1.js","w+")

f.write('var json_monitoraggio_latina_1 = '+prova)
#    for i in range(10):
#     f.write("This is line %d\r\n" % (i+1))
f.close()


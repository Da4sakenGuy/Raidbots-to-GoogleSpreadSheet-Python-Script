# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 19:15:07 2021

@author: Slater & Ghun
"""

'''
Needs to pull raidbots links from google sheets
Go into each link and scrape the item and raw dps gain
Write into the original google sheet the item name if it isn't there, if it is there then write the dps in right column
'''
import gspread
from df2gspread import df2gspread as d2g
import pandas as pd
import io
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials

def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def my_function(x):
  return list(dict.fromkeys(x))

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 
creds = ServiceAccountCredentials.from_json_keyfile_name("", scope) 
client = gspread.authorize(creds) 

spreadsheet = client.open_by_url("")
inputsheet = spreadsheet.worksheet("Sheet1")
raidCharacter, droptimizerLink = inputsheet.col_values(1), inputsheet.col_values(2)

droptimizerLinkCSV = []
for link in droptimizerLink:
    droptimizerLinkCSV.append(link + '/data.csv')   
droptimizerLinkCSV = droptimizerLinkCSV[1:]

with open('equippable-items.json', encoding="utf8") as f:
    data = json.load(f)
name_by_id = dict([(str(p['id']), p['name']) for p in data])



masterList = []
dpsGain = []
thisdict = {}
full_name2 = []
name_list = []
for CSVURL in droptimizerLinkCSV:
    url = CSVURL
    s = requests.get(url).content
    c = pd.read_csv(io.StringIO(s.decode('utf-8')))
    #print(c.to_string()) 
    
    names = c['name']
    itemID = []
    a = []
    startingDPS = c['dps_mean'][0]
    #slot = []

    dpsList = []
    name_list0 = []
    for i in range(1,len(c)):
        a = names[i].split('/')
        itemName = name_by_id[a[3]]
        itemID.append(itemName)
        #slot.append(a[5] + " " + a[6] + " " + a[1])
        dps = (c['dps_mean'][i] - startingDPS)
        full_name = itemName + " " + a[5] + " " + a[6] + " " + a[1]
        full_name2.append(full_name)
        name_list0.append(full_name)
        dpsList.append(dps)
    #remove duplicates
    dpsList = my_function(dpsList)
    dpsGain.append(dpsList)
    name_list.append(name_list0)
    masterList.append(c['name'][0])

# print(full_name)
# print('****************')
#print(name_list)
# print('****************')
#print(dpsGain)

#remove duplicates
full_name2 = my_function(full_name2)

index1 = pd.Index(full_name2)
for x in range(0,len(masterList)):
    index2 = pd.Index(name_list[x])
    notin = index1.difference(index2)
    for i in range(0, len(full_name2)):
        dpsList = []

        # not in 
        # list.index (potentially append 'Nan' to inverse indexes)
        if full_name2[i] in name_list[x]:
            dps = dpsGain[x][name_list[x].index(full_name2[i])]
            dpsList.append(int(dps))
            thisdict = add_values_in_dict(thisdict, full_name2[i], dpsList)
        if full_name2[i] in notin:
            dps = 'NaN'
            dpsList.append(dps)
            thisdict = add_values_in_dict(thisdict, full_name2[i], dpsList)
            

spreadsheet_key = ''
masterdf = pd.DataFrame(masterList, columns =['Character Name'])


# masterdf['Slot'] = pd.Series(slotcol)

# for i in range(0,len(players)):
#     name = masterList[i]
#     masterdf[players[i]] = pd.Series(name)

#need to id the item and fill in the dps from a dictionary
for i in range(0,len(full_name2)):
    masterdf[full_name2[i]] = thisdict[full_name2[i]]

#print(masterdf.to_string())
d2g.upload(masterdf, spreadsheet_key, credentials=creds, wks_name='Sheet2', col_names=True, row_names=False, clean=True)





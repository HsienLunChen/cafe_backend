import csv
import json
import os
import itertools
import requests
from difflib import SequenceMatcher
import jellyfish
import pandas as pd
import numpy as np
import sys
GoogleAPIKey = ""
# sample cafe nomad format
# {"id":"127d68b0-a3e3-4543-b161-3e3ff5e6c3d8",
# "name":"\u8389\u5712\u5546\u884c",
# "city":"taipei",
# "wifi":4,
# "seat":5,
# "quiet":4.5,
# "tasty":5,
# "cheap":2,
# "music":3,
# "url":"https:\/\/www.facebook.com\/%E8%8E%89%E5%9C%92%E5%95%86%E8%A1%8C-673209776058028\/",
# "address":"\u81fa\u5317\u5e02\u4e2d\u6b63\u5340\u4fe1\u7fa9\u8def\u4e8c\u6bb579\u5df734\u865f",
# "latitude":"25.03612600",
# "longitude":"121.52570650",
# "limited_time":"no",
# "socket":"no",
# "standing_desk":"no",
# "mrt":"\u6771\u9580",
# "open_time":""}

# total taipei cafe in nomad : 1616
# 608 currently open
# 435 not in mrt file

mrt = ['blue', 'red', 'green', 'orange', 'brown', 'circle']

n_path = "taipei.json"
mrt_path = "data_MRT"
df = None
count = 0
first = True

def all_file():
    for line in mrt:
        one_file(line)






def one_file(line):
    filename = "data_MRT/" + line + ".csv"#"data_MRT/red.csv"
    output = "data_MRT/" + line + "_integrated.csv"
    with open(filename) as mrt_file, open(output, 'w') as writer_file:
        reader = csv.DictReader(mrt_file)
        fieldname = reader.fieldnames
        fieldname.append('wifi')
        fieldname.append('quiet')
        fieldname.append('limited_time')
        fieldname.append('socket')
        print(type(fieldname))
        writer = csv.DictWriter(writer_file, fieldname)
        writer.writeheader()
        for row in reader: #itertools.islice(reader, 10):#
            #print(row['捷運站'] + row['店名']+ row['地址顛倒'])
            name = row['店名']
            add = row['地址']
            if row['地址顛倒'] == 'Y':
                # print(row['捷運站'] + row['店名']+ row['地址顛倒'])

                search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={apikey}&input={name}&inputtype={type}&fields=photos,formatted_address,name,place_id".format(apikey=GoogleAPIKey, name=name, type="textquery")
                googleResponse = requests.get(search_url)

                place_id = ""

                #print("google response: ")
                if googleResponse.status_code == requests.codes.ok:
                    googleSearchData = json.loads(googleResponse.text)
                    # print(googleSearchData)
                    candidates = googleSearchData['candidates']

                for i, c in enumerate(candidates):
                    place_id = c['place_id']
                    detail_url = "https://maps.googleapis.com/maps/api/place/details/json?key={key}&place_id={id}&language={language}&fields=name,address_components,adr_address,formatted_address,business_status".format(key=GoogleAPIKey, id=place_id, language="zh-TW")

                    detailResponse = requests.get(detail_url)

                    if detailResponse.status_code == requests.codes.ok:
                        detailData = json.loads(detailResponse.text)
                        #print("Candidate {num}:".format(num=(i+1)))
                        #print(detailData)
                        #print("Detail:")

                        # print("name:")
                        # print(detailData['result']['name'])
                        # print("formatted_address:")
                        # print(detailData['result']['formatted_address'])
                        # print("adr_address:")
                        # print(detailData['result']['adr_address'])
                        # print("address_components:")
                        # print(detailData['result']['address_components'])
                        real_add = ""
                        for component in detailData['result']['address_components'][::-1]:
                            real_add += component['long_name']
                        # print("real name: " + real_add)
                        add = real_add
            #print(name)
            store_info = in_nomad(name, add)
            row['地址'] = add
            if store_info is not None:
                row['wifi'] = store_info['wifi']
                row['quiet'] = store_info['quiet']
                row['limited_time'] = store_info['limited_time']
                row['socket'] = store_info['socket']
            writer.writerow(row)


#check the business status of certain cafe
# return the store with greatest similarity in address and not permenantly closed
def check_status(name, address, wifi, quiet, lt, socket, mrt):
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={apikey}&input={name}&inputtype={type}".format(apikey=GoogleAPIKey, name=name, type="textquery")
    best_fit = None
    best_similarity = 0

    googleResponse = requests.get(search_url)

    #print("google response: ")

    place_id = ""
    if googleResponse.status_code == requests.codes.ok:
        googleSearchData = json.loads(googleResponse.text)
        # print(googleSearchData)
        candidates = googleSearchData['candidates']
        for i, c in enumerate(candidates):
            place_id = c['place_id']
            detail_url = "https://maps.googleapis.com/maps/api/place/details/json?key={key}&place_id={id}&language={language}&fields=name,formatted_address,business_status".format(key=GoogleAPIKey, id=place_id, language="zh-TW")

            detailResponse = requests.get(detail_url)

            if detailResponse.status_code == requests.codes.ok:
                detailData = json.loads(detailResponse.text)
                similarity = jellyfish.jaro_distance(address, detailData['result']['formatted_address'])
                # print("Candidate {num}:".format(num=(i+1)))
                # #print(detailData)
                # print("Detail:")

                # print("name:")
                # print(detailData['result']['name'])
                # print("address:")
                # print(detailData['result']['formatted_address'])
                # print("similarity:")
                # #print(SequenceMatcher(None, address, detailData['result']['formatted_address']).ratio())
                # print(similarity)
                # if not (detailData['result']['business_status'] == 'CLOSED_PERMANENTLY'):
                #     print("Open")
                # else:
                #     print("CLOSED_PERMANENTLY")
                if 'business_status' in detailData['result'].keys():
                    if similarity >= best_similarity and not detailData['result']['business_status'] == 'CLOSED_PERMANENTLY' and similarity > 0.9:
                        best_fit = {'name':detailData['result']['name'], "address":detailData['result']['formatted_address'], "wifi":wifi, "quiet":quiet, "limited_time":lt, "socket":socket, "mrt":mrt}

    return best_fit


def nomad_validation():
    # search google api
    # if not permenantly closed, gain name, address from google, combine with its original plug, limited_time, wifi, quiteness


    CafeNomadAPIKey = "https://cafenomad.tw/api/v1.2/cafes/taipei/"

    cnResponse = requests.get(CafeNomadAPIKey)
    total = 0
    n_found = 0
    n_in_mrt = 0

    if cnResponse.status_code == requests.codes.ok:
        cnData = json.loads(cnResponse.text)
        #print(cnData)
        output = "data_MRT/" + "nomad.csv"
        with open(output, 'w') as writer_file:
            for shop in cnData:
                # print("==============================")
                name = shop['name']
                address = shop['address']
                wifi = shop['wifi']
                quiet = shop['quiet']
                lt = shop['limited_time']
                socket = shop['socket']
                mrt = shop['mrt']
                # print(address)

                result = check_status(name, address, wifi, quiet, lt, socket, mrt)
                if result != None:
                    total += 1
                    n_in_mrt, n_found = check_nomad_in_mrt(result, writer_file, n_in_mrt, n_found)
                    print("total: {t}, not in mrt, but in nomad: {nm}".format(t=total, nm=n_in_mrt))


#TODO don't overwrite data
def check_nomad_in_mrt(store, writer_file, n_in_mrt, n_found):
    result = None
    all_mrt = False
    output = "data_MRT/" + "nomad.csv"
    for line in mrt:
        file_exist = os.path.isfile(output)

        filename = "data_MRT/" + line + ".csv"
        with open(filename) as mrt_file:
            reader = csv.DictReader(mrt_file)
            fieldname = reader.fieldnames

            fieldname.append('wifi')
            fieldname.append('quiet')
            fieldname.append('limited_time')
            fieldname.append('socket')
            writer = csv.DictWriter(writer_file, fieldname)
            global first
            if first:
                writer.writeheader()

            found = False
            for row in reader: #itertools.islice(reader, 10):#
                if row['店名'] == store['name']:
                    found = True
                    all_mrt = True

            if not found:
                row['店名'] = store['name']
                row['地址'] = store['address']
                row['捷運站']= store['mrt']
                row['wifi'] = store['wifi']
                row['quiet'] = store['quiet']
                row['limited_time'] = store['limited_time']
                row['socket'] = store['socket']
                result = row
                #writer.writerow(row)
            first = False
    if not all_mrt and result is not None:
        writer.writerow(result)
        return n_in_mrt + 1, n_found
    else:
        return n_in_mrt, n_found +1





def name_sim(n, name):
    n_sim = jellyfish.jaro_distance(name, n)
    return n_sim

def add_sim(a, address):

    a_sim = jellyfish.jaro_distance(address, a)
    return a_sim

def in_nomad(name, address):
    # print(name)
    # print(address)
    if df is not None:
        #print(df.head(5))
        df['n_sim'] = df['name'].apply(name_sim, name=name)
        df['add_sim'] = df['address'].apply(add_sim, address=address)

        if df.loc[df['n_sim'].idxmax(), 'n_sim'] > 0.9 and df.loc[df['add_sim'].idxmax(), 'add_sim'] > 0.9 and df['n_sim'].idxmax() == df['add_sim'].idxmax():
            print("Found--------")
            print(df['n_sim'].idxmax())
            print("n_sim: "+str(df.loc[df['n_sim'].idxmax(), 'n_sim']))
            print("add_sim: "+str(df.loc[df['n_sim'].idxmax(), 'add_sim']))
            print("name: "+str(df.loc[df['n_sim'].idxmax(), 'name']))
            print("add: "+str(df.loc[df['n_sim'].idxmax(), 'address']))
            print("wifi: "+str(df.loc[df['n_sim'].idxmax(), 'wifi']))
            print("quiet: "+str(df.loc[df['n_sim'].idxmax(), 'quiet']))
            print("wifi: " + str(df.loc[df['n_sim'].idxmax(), 'limited_time']))
            print("socket: " + str(df.loc[df['n_sim'].idxmax(), 'socket']))
            global count
            count +=1
            print("=====")
            re = {
                'wifi': df.loc[df['n_sim'].idxmax(), 'wifi'],
                'quiet': df.loc[df['n_sim'].idxmax(), 'quiet'],
                'limited_time': df.loc[df['n_sim'].idxmax(), 'limited_time'],
                'socket': df.loc[df['n_sim'].idxmax(), 'socket']
            }
            return re

    return None





if __name__ == '__main__':
    with open(n_path) as nomad:
       nomad_data = json.load(nomad)
    df = pd.DataFrame(nomad_data)
    print(df.dtypes)
    print(df.shape)
    #one_file()
    #all_file()

    nomad_validation()
    # testURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={apikey}&input=良食究好市集餐廳WONMI&inputtype={type}".format(apikey=GoogleAPIKey, type="textquery")
    # googleResponse = requests.get(testURL)
    # print(json.loads(googleResponse.text))

import requests
import datetime
import json
import pandas as pd

from cowinvacc.getData import requests_url

class CowinAPIsData():
    
    def States_dict(self):
        data = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = requests_url(url)
        for i in state_name['states']:
            data.update({i['state_id']:i['state_name']})
        return data

    def States_df(self):
        data = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = requests_url(url)
        for i in state_name['states']:
            data.update({i['state_id']:i['state_name']})
        df = pd.DataFrame(list(zip(list(data.keys()), list(data.values()))), columns = ['state_id', 'state_name'])
        return df

    def States_list(self):
        data = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = requests_url(url)
        for i in state_name['states']:
            data.update({i['state_id']:i['state_name']})
        lst = list(data.values())
        return lst

    def Districts_df(self):
        data = {}
        data1 = []
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            json_data = requests_url(url)
            for i in json_data["districts"]:
                data.update({i['district_id']:i['district_name']})
                data1.append(state_code)
        df = pd.DataFrame(list(zip(list(data.keys()), data1, list(data.values()))), columns = ['district_id', 'state_code', 'district_name'])
        df.sort_values('district_id', ignore_index = True, inplace = True)
        return df

    def Districts_dict(self):
        data = {}
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            json_data = requests_url(url)
            for i in json_data["districts"]:
                data.update({i['district_id']:i['district_name']})
        return data

    def Districts_list(self):
        data = {}
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            json_data = requests_url(url)
            for i in json_data["districts"]:
                data.update({i['district_id']:i['district_name']})
        lst = list(data.values())
        return lst

    def districts_id(self, distr):
        ldist = distr.lower()
        dist_data = CowinAPIsData.Districts_dict(self)
        result = "District NOT found, search using Districts_list()."
        for i in list(dist_data.values()):
            if ldist in i.lower():
                key_dist = list(dist_data.keys())[list(dist_data.values()).index(i)]
                result = "District Code for {} is {}".format(i, key_dist)
        return result
            

    

    

    



    




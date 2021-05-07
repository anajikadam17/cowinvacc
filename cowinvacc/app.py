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

    def centersBydistId(self, district_id, numdays=5):
        df = pd.DataFrame(columns = ['date', 'center_id', 'name', 'address',
                                'state_name', 'district_name', 'block_name', 'pincode',
                                    'from1', 'to', 'fee_type', 'available_capacity', 'min_age_limit', 'vaccine', 'slots'])
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for INP_DATE in date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, INP_DATE)
            #print(URL)
            json_data = requests_url(URL)
            if type(json_data)==dict:
                if json_data["centers"]:
                    for center in json_data["centers"]:
                        date = center['sessions'][0]['date']
                        center_id = center['center_id']
                        name = center['name']
                        address = center['address']
                        state_name = center['state_name']
                        district_name = center['district_name']
                        block_name = center['block_name']
                        pincode = center['pincode']
                        from1 = center['from']
                        to = center['to']
                        fee_type = center['fee_type']
                        available_capacity = center['sessions'][0]['available_capacity']
                        min_age_limit = center['sessions'][0]['min_age_limit']
                        vaccine = center['sessions'][0]['vaccine']
                        slots = center['sessions'][0]['slots']
                        df.loc[len(df)] = [date, center_id, name, address,state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
                else:
                    #print("No available slots on {}".format(INP_DATE))
                    date = INP_DATE
                    center_id = 'NA'
                    name = 'NA'
                    address = 'NA'
                    state_name = 'NA'
                    district_name = 'NA'
                    block_name = 'NA'
                    pincode = 'NA'
                    from1 = 'NA'
                    to = 'NA'
                    fee_type = 'NA'
                    available_capacity = 'NA'
                    min_age_limit = 'NA'
                    vaccine = 'NA'
                    slots = 'NA'
                    df.loc[len(df)] = [date, center_id, name, address,
                                        state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
        return df


    def centersByPinCode(self, POST_CODE, numdays=5):
        POST_CODE = str(POST_CODE)
        df = pd.DataFrame(columns = ['date', 'center_id', 'name', 'address',
                                'state_name', 'district_name', 'block_name', 'pincode',
                                    'from1', 'to', 'fee_type', 'available_capacity', 'min_age_limit', 'vaccine', 'slots'])
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for INP_DATE in date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
            #print(URL)
            json_data = requests_url(URL)
            if type(json_data)==dict:
                if json_data["centers"]:
                    for center in json_data["centers"]:
                        date = center['sessions'][0]['date']
                        center_id = center['center_id']
                        name = center['name']
                        address = center['address']
                        state_name = center['state_name']
                        district_name = center['district_name']
                        block_name = center['block_name']
                        pincode = center['pincode']
                        from1 = center['from']
                        to = center['to']
                        fee_type = center['fee_type']
                        available_capacity = center['sessions'][0]['available_capacity']
                        min_age_limit = center['sessions'][0]['min_age_limit']
                        vaccine = center['sessions'][0]['vaccine']
                        slots = center['sessions'][0]['slots']
                        df.loc[len(df)] = [date, center_id, name, address,state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
                else:
                    #print("No available slots on {}".format(INP_DATE))
                    date = INP_DATE
                    center_id = 'NA'
                    name = 'NA'
                    address = 'NA'
                    state_name = 'NA'
                    district_name = 'NA'
                    block_name = 'NA'
                    pincode = 'NA'
                    from1 = 'NA'
                    to = 'NA'
                    fee_type = 'NA'
                    available_capacity = 'NA'
                    min_age_limit = 'NA'
                    vaccine = 'NA'
                    slots = 'NA'
                    df.loc[len(df)] = [date, center_id, name, address,
                                        state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
        return df
    
            

    

    

    



    




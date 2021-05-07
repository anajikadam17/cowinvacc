# Cowin Tracker for Covid-19 vaccine usng CoWin API's.

Python API wrapper for CoWin, India's digital platform launched by the government to help citizens register themselves for the vaccination drive by booking an appointment at the nearby vaccination centres.
This python wrapper is used  for find centers for vaccine availablity either in a district or in a particular pin code using district id or pin code and number of days as input.

Example:

```python
from cowinvacc import CowinAPIsData

obj = CowinAPIsData()

states_dict = obj.States_dict()
print(states_dict)
```

# Install

`pip install cowinvacc`

# Usage

The wrapper currently covers nine endpoints used by the CoWin portal specified below.

## Initialize

```python
from cowinvacc import CowinAPIsData

obj = CowinAPIsData()
```

## Get all the available states in Dictionary

Returns the dictionary of states in which vaccine drive is being conducted. In dictionary `state_id` as key and `state_name` as value.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

states_dict = obj.States_dict()
print(states_dict)
```

## Get all the available states in List

Returns the List of states in which vaccine drive is being conducted.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

states_list = obj.States_list()
print(states_list)
```

## Get all the available states in DataFrame

Returns the DataFrame of states in which vaccine drive is being conducted. In DataFrame contain columns as `state_id`  and `state_name`.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

states_df = obj.States_df()
print(states_df)
```

## Get all the available Districts in Dictionary

Returns the dictionary of Districts in which vaccine drive is being conducted. In dictionary `district_id` as key and `district_name` as value.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

districts_dict = obj.Districts_dict()
print(districts_dict)
```

## Get all the available Districts in List

Returns the List of Districts in which vaccine drive is being conducted.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

districts_list = obj.Districts_list()
print(districts_list)
```

## Get all the available Districts in DataFrame

Returns the DataFrame of Districts in which vaccine drive is being conducted. In DataFrame contain columns as `district_id `, `state_code`  and `district_name`.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

dist_df = obj.Districts_df()
print(dist_df)
```

## Get Districts name and District ID with district name as input

Returns the Districts name and District ID in which vaccine drive is being conducted, Input as district name.
```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

randomDist = 'kolh'
district_name = obj.districts_id(randomDist)
print(district_name)
```

## Get all the available centers in DataFrame with district id as input

Returns the DataFrame of centers in which vaccine drive is being conducted. Input as district_id and numdays(optional), default numdays is 5.
In DataFrame contain columns as date, center_id, center name, center address, state_name, district_name, center block_name, pincode, from time, to time, fee_type, available_capacity, min_age_limit, vaccine name and slots.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

district_id = 372
numdays = 5
df1 = obj.centersBydistId(district_id, numdays)
print(df1)
```

## Get all the available centers in DataFrame with POST_CODE as input

Returns the DataFrame of centers in which vaccine drive is being conducted. Input as POST_CODE and numdays(optional), default numdays is 5.
In DataFrame contain columns as date, center_id, center name, center address, state_name, district_name, center block_name, pincode, from time, to time, fee_type, available_capacity, min_age_limit, vaccine name and slots.

```python
from cowinvacc import CowinAPIsData
obj = CowinAPIsData()

numdays = 6
POST_CODE = 415709
df2 = obj.centersByPinCode(POST_CODE, numdays)
print(df2)
```

# Notes

The API's of CoWin may at times return a 401 Unauthorized response. To mitigate this we are passing user agents in the
request. Still, if the issue persists please wait for a few minutes before trying again.

Please try not to spam the CoWin servers and try to keep a timeout between subsequent requests if you are polling at a
fixed interval


Please feel free to give your suggestions for improvement.

---

# License

MIT License

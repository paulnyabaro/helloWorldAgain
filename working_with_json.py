import json, requests, sys

# string_of_json_data = open('string_of_json_data.json')
#
# json_data_in_python = json.loads('string_of_json_data.json')
# print(json_data_in_python)

url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3'
response = requests.get(url)
response.raise_for_status()

# Then load the data using json.loads()
# And finally print it using pprint.pprint()
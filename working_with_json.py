import json, requests

# string_of_json_data = open('string_of_json_data.json')
#
# json_data_in_python = json.loads('string_of_json_data.json')
# print(json_data_in_python)

url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Then load the data using json.loads()
# And finally print it using pprint.pprint()

weather_data = json.loads(response.text)
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
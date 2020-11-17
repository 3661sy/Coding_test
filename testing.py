import json

data = '{"car":[{"accident": false, "repair": "text", "manufacturer": "other", "price": 1400}, {"accident": true, "repair": " ", "manufacturer": "Hundai", "price": 1200}]}'
json_data = json.loads(data)

print(json_data['car'])

for i in json_data['car']:
    print(i['accident'])
    print(i['repair'])
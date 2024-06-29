import requests


url='https://queue-times.com/parks/2/queue_times.json'

response = requests.get(url)

#print(response.status_code)

#print(response.json())
#print(response.json()['lands'][0]['rides'])

for ride in response.json()['lands'][0]['rides']:
  if ride['is_open']==True:
    print(ride['name'],'-',ride['wait_time'])

import requests

url = 'https://github.com/timeline.json'
#url = 'http://sample-file.bazadanni.com/download/txt/json/sample.json'
#url = 'http://mtgjson.com/json/AllSets.json'

r = requests.get(url)
print r
json_obj = r.json()

repos = set() # we want just unique urls
for entry in json_obj:
    try:
        repos.add(entry['repository']['url'])
    except KeyError as e:
        print "No key %s. Skipping..." % (e)

from pprint import pprint 
pprint(repos)

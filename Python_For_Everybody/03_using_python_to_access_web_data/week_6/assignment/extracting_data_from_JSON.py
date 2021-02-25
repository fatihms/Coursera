
# Extracting Data from JSON

'''
 Extracting Data from JSON

 In this assignment you will write a Python program somewhat similar 
 to http://www.py4e.com/code3/json2.py. The program will prompt for a 
 URL, read the JSON data from that URL using urllib and then parse and 
 extract the comment counts from the JSON data, compute the sum of the 
 numbers in the file and enter the sum below:

 Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location:')
print('Retrieving', location)

uh = urllib.request.urlopen(location, context=ctx)
data = uh.read()

info = json.loads(data)

count = 0
total = 0

for item in info['comments']:
    total += int(item['count'])
    count += 1

print('Count: ', count)
print('Sum: ', total)
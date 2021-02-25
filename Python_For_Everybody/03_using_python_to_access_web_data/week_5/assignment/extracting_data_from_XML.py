# Extracting Data from XML

'''
 Extracting Data from XML

 In this assignment you will write a Python program somewhat similar 
 to http://www.py4e.com/code3/geoxml.py. The program will prompt for 
 a URL, read the XML data from that URL using urllib and then parse 
 and extract the comment counts from the XML data, compute the sum of the numbers in the file.

 Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

location = input('Enter location: ')

uh = urllib.request.urlopen(location, context=ctx)
data = uh.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

for item in lst:
    count = item.find('count').text
    total += int(count)

print(total)
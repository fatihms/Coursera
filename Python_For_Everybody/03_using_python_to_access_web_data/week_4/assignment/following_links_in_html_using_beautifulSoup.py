# Assignment: Following Links in HTML Using BeautifulSoup

'''
 Open the file mbox-short.txt and read it line by line. 
 When you find a line that starts with 'From ' like the following line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

 You will parse the From line using split() and print out the second 
 word in the line (i.e. the entire address of the person who sent the message). 
 Then print out a count at the end.
 Hint: make sure not to include the lines that start with 'From:'. 
 Also look at the last line of the sample output to see how to print the count.

 You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

i = 0
while i < count:

  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Retrieve all of the anchor tags
  tags = soup('a')
  print('Retrieving:', tags[position - 1].get('href', None))
  url = tags[position - 1].get('href', None)

  i += 1
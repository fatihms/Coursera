# Extracting Data With Regular Expressions

'''
 Finding Numbers in a Haystack

 In this assignment you will read through and parse a file with text and numbers. 
 You will extract all the numbers in the file and compute the sum of the numbers.
'''
 
import re
hand = open ('regex_sum_42.txt')
lst = list()
total = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0:
        continue
    for num in stuff:
        total += int(num)
        
print(total)
import string
import re

def searchForBag(values, searchFor, result=None):
    if (result is None):
        result = []
    bagsFound = 0
    for k in values:
        for v in values[k]:
            for string in searchFor:
                if string in v and str(k).strip() not in result:
                    result.append(k.strip())
                    bagsFound += 1
                    result = list(set(result))
    if(bagsFound == 0):
        return result
    else:
        return searchForBag(values, result, result)

with open('input.txt', 'r') as data:
    data = [line.rstrip('\n') for line in data]

bags = {}
pattern = re.compile("\\b(bag|bags)\\W", re.I)
for bag in data:
    temp = bag.split('contain')[1].strip().split(',')
    temp = [x.translate(str.maketrans('', '', string.punctuation)) for x in temp]
    temp = [x.rsplit(' ', 1)[0] for x in temp]
    bags[bag.split('bags')[0].strip()] = temp

print(len(searchForBag(bags, ['shiny gold'])))
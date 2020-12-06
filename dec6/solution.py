
from collections import Counter

with open('input.txt', 'r') as data:
    data = [line.split() for line in data.read().split('\n\n')]

combined_data = []
for group in data:
    combined_group = []
    for person in group:
        combined_group += list(person)
    combined_data.append(combined_group)

total_yes = 0
for group in combined_data:
    group = set(group)
    total_yes += len(group)
print(total_yes)

combined_data_with_count = {}
counter = 0
for group in data:
    combined_group = []
    for person in group:
        combined_group += list(person)
    combined_data_with_count[str(len(group)) + '_' + str(counter)] = (combined_group)
    counter += 1

total_yes_2 = 0
for test in combined_data_with_count.keys():
    total_yes_2 += sum( x == int(test.split('_')[0]) for x in Counter(combined_data_with_count[test]).values() )
print(total_yes_2)

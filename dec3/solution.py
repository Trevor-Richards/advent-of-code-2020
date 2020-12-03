with open('input.txt', 'r') as data:
    data = [line.rstrip('\n') for line in data]

row_incrementer = 0
column_incrementer = 0
trees_hit = 0
for row in range(len(data) - 1):
    row_incrementer += 1
    column_incrementer += 3
    #Wrap incrementer around each line as they just repeat
    if (column_incrementer % 31 != column_incrementer):
        column_incrementer = column_incrementer % 31
    if (data[row_incrementer][column_incrementer] == '#'):
        trees_hit += 1

print(trees_hit)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
final_multiplier = 1
for slope in slopes:
    trees_hit_2 = 0
    row_incrementer_2 = 0
    column_incrementer_2 = 0
    x, y = slope
    for row in range(len(data) - 1):
        row_incrementer_2 += y
        column_incrementer_2 += x
        if (row_incrementer_2 > 322):
            break
        #Wrap incrementer around each line as they just repeat
        if (column_incrementer_2 % 31 != column_incrementer_2):
            column_incrementer_2 = column_incrementer_2 % 31
        if (data[row_incrementer_2][column_incrementer_2] == '#'):
            trees_hit_2 += 1
    final_multiplier *= trees_hit_2

print(final_multiplier)


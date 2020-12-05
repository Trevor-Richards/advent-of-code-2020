with open('input.txt', 'r') as data:
    data = [line.rstrip('\n') for line in data]

def find_row(row_sequence):
    inital_range = [*range(128)]
    for char in list(row_sequence):
        if (char == 'F'):
            inital_range = inital_range[:len(inital_range)//2]
        elif (char == 'B'):
            inital_range = inital_range[len(inital_range)//2:]
    return inital_range[0]

def find_column(column_sequence):
    inital_range = [*range(8)]
    for char in list(column_sequence):
        if (char == 'L'):
            inital_range = inital_range[:len(inital_range)//2]
        elif (char == 'R'):
            inital_range = inital_range[len(inital_range)//2:]
    return inital_range[0]

seat_ids = []
for line in data:
    row = find_row(line[:-3])
    column = find_column(line[7:])
    seat_ids.append(int(row) * 8 + int(column))

seat_ids.sort()
my_seat_id = sorted(set(range(seat_ids[0], seat_ids[-1] + 1)).difference(seat_ids))
print(seat_ids[-1])
print(my_seat_id[0])



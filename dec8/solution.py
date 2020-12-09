with open('input.txt', 'r') as data:
    data = [line.rstrip('\n') for line in data]

lines_executed = []
line = 0
acc = 0

while len(lines_executed) == len(set(lines_executed)):
    if data[line].split(' ')[0] == 'nop':
        line += 1
    elif data[line].split(' ')[0] == 'acc':
        if data[line].split(' ')[1][0] == '+':
            acc += int(data[line].split(' ')[1].split('+')[1])
        elif data[line].split(' ')[1][0] == '-':
            acc -= int(data[line].split(' ')[1].split('-')[1])
        line += 1
    elif data[line].split(' ')[0] == 'jmp':
        if data[line].split(' ')[1][0] == '+':
            line += int(data[line].split(' ')[1].split('+')[1])
        elif data[line].split(' ')[1][0] == '-':
            line -= int(data[line].split(' ')[1].split('-')[1])
    lines_executed.append(line)

print(acc)

solution_found = False
for i in range(len(data)):
    lines_executed_2 = []
    line = 0
    acc = 0
    if data[i].split(' ')[0] == 'nop':
        data[i] = data[i].replace('nop', 'jmp')
    elif data[i].split(' ')[0] == 'jmp':
        data[i] = data[i].replace('jmp', 'nop')
    while len(lines_executed_2) == len(set(lines_executed_2)):
        if(line == len(data)):
            solution_found = True
            break
        if data[line].split(' ')[0] == 'nop':
            line += 1
        elif data[line].split(' ')[0] == 'acc':
            if data[line].split(' ')[1][0] == '+':
                acc += int(data[line].split(' ')[1].split('+')[1])
            elif data[line].split(' ')[1][0] == '-':
                acc -= int(data[line].split(' ')[1].split('-')[1])
            line += 1
        elif data[line].split(' ')[0] == 'jmp':
            if data[line].split(' ')[1][0] == '+':
                line += int(data[line].split(' ')[1].split('+')[1])
            elif data[line].split(' ')[1][0] == '-':
                line -= int(data[line].split(' ')[1].split('-')[1])
        lines_executed_2.append(line)
    if solution_found:
        print(acc)
        break
    if data[i].split(' ')[0] == 'nop':
        data[i] = data[i].replace('nop', 'jmp')
    elif data[i].split(' ')[0] == 'jmp':
        data[i] = data[i].replace('jmp', 'nop')

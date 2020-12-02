input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

solution_found = False

for num in contents_split:
    arrayToTestAgainst = contents_split[:]
    arrayToTestAgainst.remove(num)
    for num2 in arrayToTestAgainst:
        if(int(num) + int(num2) == 2020):
            solution_found = True
            print(int(num) * int(num2))
            break
    if(solution_found):
        break

solution_found_2 = False

for num in contents_split:
    if (solution_found_2):
        break
    contents_split_2 = contents_split[:]
    contents_split_2.remove(num)
    for num2 in contents_split_2:
        if(solution_found_2):
            break
        contents_split_3 = contents_split_2[:]
        contents_split_3.remove(num2)
        for num3 in contents_split_3:
            if(int(num) + int(num2) + int(num3) == 2020):
                print(int(num) * int(num2) * int(num3))
                solution_found_2 = True
                break

from collections import Counter

input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

passwords = []

for line in contents_split:
    passwords.append({
        'char_min': line.split('-')[0].strip(),
        'char_max': line.split('-')[1].split(' ')[0].strip(),
        'char_value': line.split(' ')[1].split(':')[0].strip(),
        'pass_value': line.split(':')[1].strip()
    })

valid_passwords = 0

for password in passwords:
    password_count = Counter(password['pass_value'])
    if (password['char_value'] in password_count and (int(password['char_min']) <= int(password_count[password['char_value']]) <= int(password['char_max']))):
        valid_passwords += 1

print(valid_passwords)

valid_passwords_2 = 0

for password in passwords:
    if ((password['pass_value'][int(password['char_min']) - 1] == password['char_value']) is not (password['pass_value'][int(password['char_max']) - 1] == password['char_value'])):
        valid_passwords_2 += 1

print(valid_passwords_2)

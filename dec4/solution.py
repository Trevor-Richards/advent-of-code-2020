import re

def additional_validation(passport):
    conditions = [check_byr, check_iyr, check_eyr, check_hgt, check_hcl, check_ecl, check_pid]
    return all(condition(passport) for condition in conditions)

def check_byr(passport):
    return True if (len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002) else False
def check_iyr(passport):
    return True if (len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020) else False
def check_eyr(passport):
    return True if (len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030) else False
def check_hgt(passport):
    return True if ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)) else False
def check_hcl(passport):
    pattern = re.compile("[a-f0-9]+")
    return True if (passport['hcl'][0] == '#' and pattern.fullmatch(passport['hcl'][1:]) is not None) else False
def check_ecl(passport):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return True if (passport['ecl'] in valid_ecl) else False
def check_pid(passport):
    return True if (len(passport['pid']) == 9) else False

with open('input.txt', 'r') as data:
    data = [line.split() for line in data.read().split('\n\n')]

valid_part_1 = 0
valid_part_2 = 0
passports = []
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in data:
    passportDic = {}
    for field in passport:
        passportDic.update({field.split(':')[0]:field.split(':')[1]})
    passports.append(passportDic)

for passport in passports:
    if (set(required_fields).issubset(set(list(passport.keys())))):
        valid_part_1 += 1
        if(additional_validation(passport)):
            valid_part_2 += 1

print (valid_part_1)
print (valid_part_2)

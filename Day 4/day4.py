from passport import Passport

#Day 4 

5
INPUT_DATA_LOCATION = "Data/day4_data.txt"

passports = []
current_passport_data = []
number_of_valid_passports_part1 = 0
number_of_valid_passports_part2 = 0

inputData = open(INPUT_DATA_LOCATION, 'r')
line = inputData.readline()


while line:
    if line == "\n":
        passports.append(Passport(current_passport_data))
        current_passport_data = []
    else:
        current_passport_data.append(line)
    line = inputData.readline()
inputData.close()
passports.append(Passport(current_passport_data))

for passport in passports:
    if passport.checkPassportIsComplete() == True:
        number_of_valid_passports_part1 += 1

for passport in passports:
    if passport.is_valid == True:
        number_of_valid_passports_part2 += 1


print(f"Number of valid passports for part 1: {number_of_valid_passports_part1}")
print(f"Number of valid passports for part 2: {number_of_valid_passports_part2}")
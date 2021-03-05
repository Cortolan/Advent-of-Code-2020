# Day 1, read all numbers find 2 that add to the value of 2020 and then print the multiple of them
VALUE =2020

numbers = []
multipleOfTwoNumbers = 0
multipleOfThreeNumbers = 0

inputData = open("data/day1_data.txt", 'r')
line = inputData.readline()
while line:
    numbers.append(line)
    line = inputData.readline()
inputData.close()

for i in numbers:
	for j in numbers:
		if int(i) + int(j) == VALUE:
			multipleOfTwoNumbers =(int(i)*int(j))

for i in numbers:
	for j in numbers:
		for k in numbers:
			if int(i) + int(j) + int(k) == VALUE:
				multipleOfThreeNumbers =(int(i)*int(j)* int(k))


print("Multiple of twos: ", multipleOfTwoNumbers)
print("Multiple of three numbers: ", multipleOfThreeNumbers)
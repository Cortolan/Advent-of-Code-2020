#Day 2 Verify Password Requirments 
passwordTypeOneCount = 0
passwordTypeTwoCount = 0

def checkData(unparsedData):
    global passwordTypeOneCount
    global passwordTypeTwoCount
    
    splitUnparsedData = unparsedData.split(' ', 2)
    keyValues = splitUnparsedData[0].split('-', 1)
    key = splitUnparsedData[1]
    password = splitUnparsedData[2]

    if checkPasswordTypeOne(keyValues, key[0], password) == True:
        passwordTypeOneCount += 1
    if checkPasswordTypeTwo(keyValues, key[0], password) == True:
        passwordTypeTwoCount += 1


#Part 1 Password Check Function        
def checkPasswordTypeOne(keyValues, key, password):
    numberOfChars = 0

    for char in password:
        if char == key:
            numberOfChars += 1
    
    if numberOfChars >= int(keyValues[0]) and numberOfChars <= int(keyValues[1]):
        return True
    else: False

#Part 2 Password Check Function
def checkPasswordTypeTwo(keyValues, key, password):
    if password[int(keyValues[0])-1] == key or password[int(keyValues[1])-1] == key:
        if password[int(keyValues[0])-1] == key and password[int(keyValues[1])-1] == key:
            return False
        else:
            return True
    else:
        return False
    
inputData = open("data/day2_data.txt", 'r')
line = inputData.readline()
while line:
    checkData(line)
    line = inputData.readline()
inputData.close()

print ("Number of type 1 passwords: ", passwordTypeOneCount)
print ("Number of type 2 passwords: ", passwordTypeTwoCount)
#Day 3 Tobogan 
#Part 1 Navigate down hill moving down 1 to the right 3. count how many trees you encounter
#Part 2 try Several diffrent pathts and multiple trees encountered together
INPUT_DATA_LOCATION = "data/day3_data.txt"

hillCostMap = []
position = (0,0)

def moveDownHill(downAmount, accrossAmount):
    global position
    xPosition = position[0]
    yPosition = position[1]

    # -1 to make it 0-30, additional -1 becase it loads a \n from the textfile in sameple data
    widthOfHill = len(hillCostMap[0]) -2 

    if xPosition + accrossAmount > widthOfHill:
        # -1 to keep overlap to go to zero instead of 1 
        xPosition += accrossAmount - 1 - widthOfHill 
    else:
        xPosition += accrossAmount
    
    if (yPosition + downAmount) >= len(hillCostMap):
        yPosition = len(hillCostMap)
    else:
        yPosition += downAmount

    position = (xPosition, yPosition)

def testMovement(downAmount, accrossAmount):
    treesHit = 0
    heightOfHill = int((len(hillCostMap)/downAmount))
    global position 
    position = (0,0)

    for i in range(0, heightOfHill):
        if hillCostMap[position[1]][position[0]] == '#':
            treesHit +=1    
        moveDownHill(downAmount,accrossAmount)

    print(f"({downAmount},{accrossAmount}), Number of trees hit: {treesHit}")
    return treesHit   


inputData = open(INPUT_DATA_LOCATION, 'r')
line = inputData.readline()
while line:
    hillCostMap.append(line)
    line = inputData.readline()
inputData.close()


testResults = []

testResults.append(testMovement(1,1))
testResults.append(testMovement(1,3)) #Part 1
testResults.append(testMovement(1,5))
testResults.append(testMovement(1,7))
testResults.append(testMovement(2,1))

totalTreesHitMultiplied = testResults[0]

for test in range(1, len(testResults)):
    totalTreesHitMultiplied = totalTreesHitMultiplied * testResults[test]

print(f"\nAll tests multiplied = {totalTreesHitMultiplied}")



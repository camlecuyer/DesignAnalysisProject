import random
import copy

zip = []
MIN_WEIGHT = 1
MAX_WEIGHT = 10

with open('zipcodes.txt','r') as file:
    for line in file:
        data = line.rstrip()
        zip.append(data)
file.close()

#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
# for matrix initialization

size = len(zip)
#size = 5

zipMatrix = [[0 for x in range(size)] for y in range(size)]

#print(zipMatrix)

maxConnections = size / 5

#randomly choose number of children between 1 and 20% of zip for every node
for i in range(size):
    numConn = random.randint(1, maxConnections)
    connList = random.sample(range(0, size), numConn)

    for j in range(len(connList)):
        if i != connList[j]:
            weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
            zipMatrix[i][connList[j]] = weight
            zipMatrix[connList[j]][i] = weight

#https://stackoverflow.com/questions/21547462/how-to-multiply-2-dimensional-arrays-matrix-multiplication
def connectMatrix(connectMatrix, adjMatrix, mSize):
    result = [[0 for x in range(mSize)] for y in range(mSize)]
    for i in range(mSize):
        for j in range(mSize):
            for k in range(mSize):
                result[i][j] += adjMatrix[i][k] * connectMatrix[k][j]

            if result[i][j] != 0:
                result[i][j] = 1

    return result

checkMatrix = [[0 for x in range(size)] for y in range(size)]

for i in range(size):
    for j in range(size):
        if (0 != zipMatrix[i][j]) or (i == j):
            checkMatrix[i][j] = 1
            
#print(zipMatrix)
#print(checkMatrix)

zeroFound = True

while zeroFound:
    connMatrix = copy.deepcopy(checkMatrix)

    zeroIndexX = 0
    zeroIndexY = 0
    
    for i in range(size):
        zeroFound = False
        connMatrix = copy.deepcopy(connectMatrix(connMatrix, checkMatrix, size))
        for j in range(size):
            for k in range(size):
                if connMatrix[j][k] == 0:
                    zeroFound = True
                    zeroIndexX = j
                    zeroIndexY = k
                    break
            if zeroFound:
                break
        if not zeroFound:
            break
        
    if zeroFound:
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        zipMatrix[zeroIndexX][zeroIndexY] = weight
        zipMatrix[zeroIndexY][zeroIndexX] = weight
        checkMatrix[zeroIndexX][zeroIndexY] = 1
        checkMatrix[zeroIndexY][zeroIndexX] = 1
        #print(zipMatrix)

print(connMatrix)
print(zipMatrix)
            
out =  open('graph.csv', 'w')

for i in range(size):
    for j in range(size):
        if zipMatrix[i][j] != 0:
            out.write(zip[i] + "," + zip[j] + "," + str(zipMatrix[i][j]) + "\n")
out.close()

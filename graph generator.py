import random

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

zipMatrix = [[0 for x in range(size)] for y in range(size)]

#print(zipMatrix)

maxConnections = size / 5

#randomly choose number of children between 1 and 20% of zip for every node
for i in range(size):
    numConn = random.randint(1, maxConnections)
    connList = random.sample(range(0, 50), numConn)

    for j in range(len(connList)):
        if i != connList[j]:
            weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
            zipMatrix[i][connList[j]] = weight
            zipMatrix[connList[j]][i] = weight
            
out =  open('graph.csv', 'w')

for i in range(size):
    for j in range(size):
        if zipMatrix[i][j] != 0:
            out.write(zip[i] + "," + zip[j] + "," + str(zipMatrix[i][j]) + "\n")
out.close()

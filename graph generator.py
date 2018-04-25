import random
import copy

zip = []

# constants for the min and max edge weight
MIN_WEIGHT = 1
MAX_WEIGHT = 10

# reads in the zipcodes
with open('zipcodes.txt','r') as file:
#with open('zipcodesMedTest.txt','r') as file:
    for line in file:
        data = line.rstrip()
        zip.append(data)
file.close()

# number of zipcodes in list
size = len(zip)
#size = 5

# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
# the above URL is where I found the code for 2D matrix initialization
zipMatrix = [[0 for x in range(size)] for y in range(size)]

#print(zipMatrix)

# generates the maximum number of connections generated per node, the max is about 20% of the number of zipcodes
maxConnections = size / 5
#maxConnections = 1

# loops through each node and generates the number of connections per node, and the nodes destinations
for i in range(size):
    numConn = random.randint(1, maxConnections)
    connList = random.sample(range(0, size), numConn)

    # loops through the destinations, and randomly generates the weight, and then assigns the weights in an
    # undirected fashion using both nodes as start and end, only leaving out a connection if the node points to itself
    for j in range(len(connList)):
        if i != connList[j]:
            weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
            zipMatrix[i][connList[j]] = weight
            zipMatrix[connList[j]][i] = weight

# https://stackoverflow.com/questions/21547462/how-to-multiply-2-dimensional-arrays-matrix-multiplication
# the above URL provided the base function for multiplying 2 matricies
# this function multiplies two square matricies and saves the result in a matrix of the same size
def connectMatrix(connectMatrix, adjMatrix, mSize):
    result = [[0 for x in range(mSize)] for y in range(mSize)]
    for i in range(mSize):
        for j in range(mSize):
            for k in range(mSize):
                result[i][j] += adjMatrix[i][k] * connectMatrix[k][j]

            # after multiplying the data, it checks to see if there is a connection, and sets the value to 1
            # in order to prevent large numbers from being inserted into the matrix, and slowing processing
            if result[i][j] != 0:
                result[i][j] = 1

    return result

# creates the adjacency matrix
checkMatrix = [[0 for x in range(size)] for y in range(size)]

# fills the adjacency matrix, and sets connections to a node equal to 1, and sets the diagonal to 1
for i in range(size):
    for j in range(size):
        if (0 != zipMatrix[i][j]) or (i == j):
            checkMatrix[i][j] = 1
            
#print(zipMatrix)
#print(checkMatrix)

# flag to control the loops
zeroFound = True

# runs through mutliplying the matricies until every node can reach every other node
while zeroFound:
    # copies the adjacency matrix into a second matrix that will be changed in the loop
    connMatrix = copy.deepcopy(checkMatrix)

    # holdes the index for any zero found
    zeroIndexX = 0
    zeroIndexY = 0

    # does matrix multiplication equal to the number of nodes, to check if a node can reach all other nodes
    for i in range(size):
        zeroFound = False
        # matrix mulitplication step
        connMatrix = copy.deepcopy(connectMatrix(connMatrix, checkMatrix, size))

    # checks the matrix for a zero, if one is found, it breaks out of the loop
    for j in range(size):
        for k in range(size):
            if connMatrix[j][k] == 0:
                zeroFound = True
                zeroIndexX = j
                zeroIndexY = k
                break
        if zeroFound:
            break
        #if not zeroFound:
            #break

    # if a zero is found, insert a connection to that node
    if zeroFound:
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        zipMatrix[zeroIndexX][zeroIndexY] = weight
        zipMatrix[zeroIndexY][zeroIndexX] = weight
        checkMatrix[zeroIndexX][zeroIndexY] = 1
        checkMatrix[zeroIndexY][zeroIndexX] = 1
        #print(zipMatrix)

#print(connMatrix)
#print(zipMatrix)

# print out the graph to a file
out =  open('graph.csv', 'w')
#out =  open('graphMedTest.csv', 'w')

for i in range(size):
    for j in range(size):
        if zipMatrix[i][j] != 0:
            out.write(zip[i] + "," + zip[j] + "," + str(zipMatrix[i][j]) + "\n")
out.close()

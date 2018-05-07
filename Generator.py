import random
import copy

class Generator():
    def __init__(self, size):
        self.zip = []
        self.zipSize = 0
        
        # ranges for zipcode sample
        self.UPPER_RANGE = 66000
        self.LOWER_RANGE = 64000

        # constants for vehicles identification
        self.AMBULANCE = 1
        self.FIRE_TRUCK = 2
        self.POLICE_CAR = 3

        # constants for the min and max edge weight
        self.MIN_WEIGHT = 1
        self.MAX_WEIGHT = 10

        self.generateZip(size)
        self.generateRequests()
        self.generateGraph()
    
    # takes in a range of data and samples random zipcodes from that range based on size
    def generateZip(self, size):
        self.zip = random.sample(range(self.LOWER_RANGE,  self.UPPER_RANGE), size)
        #print(data)
        
        # sorts the data
        self.zip.sort()
        #print(data)

        self.zipSize = len(self.zip)

        # outputs the data to file: zipcodes.txt with end line characters after each zipcode
        file =  open('zipcodes.txt', 'w')
        #file =  open('zipcodesMedTest.txt', 'w')

        for zcode in self.zip:
            file.write(str(zcode) + "\n")

        file.close()

    def generateRequests(self):
        # randomly selects a number between 2 and 5
        # the number is then multiplied by self.zipSize to determine the number of requests and vehicles
        requestNumSize = random.randint(2, 5)
        #requestNumSize = 1
        requestNum = self.zipSize * requestNumSize

        # totals of each type of vehicle
        total_police = 0
        total_firetruck = 0
        total_ambulance = 0

        # outputs the requests and vehicles to separate files
        out =  open('requests.csv', 'w')
        outV = open('vehicles.csv', 'w')
        #out =  open('requestsMedTest.csv', 'w')
        #outV = open('vehiclesMedTest.csv', 'w')

        out.write("request_ID,type,location\n");
        outV.write("vehicle_ID,type,location\n");

        # loops through the number of requests, and randomly generates the vehicle required,
        # the location of the request, and generates a different location for the vehicle to start at
        for i in range(requestNum):
            request = random.randint(0, self.zipSize - 1)
            vehicleLoc = random.randint(0, self.zipSize - 1)
            vehicle = random.randint(1,3)

            # increases the total vehicles
            if vehicle == self.AMBULANCE:
                total_ambulance += 1
            elif vehicle == self.FIRE_TRUCK:
                total_firetruck += 1
            else:
                total_police += 1

            #print(str(i + 1) + "," + str(vehicle) + "," + self.zipzip[request])

            # outputs the results their respective file    
            out.write(str(i + 1) + "," + str(vehicle) + "," + str(self.zip[request]) + "\n")
            outV.write(str(i + 1) + "," + str(vehicle) + "," + str(self.zip[vehicleLoc]) + "\n")
        out.close()
        outV.close()

        # outputs the totals to a separate file
        out =  open('requestNum.txt', 'w')
        #out =  open('requestNumMedTest.txt', 'w')

        out.write(str(total_ambulance) + "," + str(total_firetruck) + "," + str(total_police) + "\n")

        out.close()

    def generateGraph(self):
        # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        # the above URL is where I found the code for 2D matrix initialization
        zipMatrix = [[0 for x in range(self.zipSize)] for y in range(self.zipSize)]

        #print(zipMatrix)

        # generates the maximum number of connections generated per node, the max is about 20% of the number of zipcodes
        maxConnections = self.zipSize / 5
        #maxConnections = 1

        # loops through each node and generates the number of connections per node, and the nodes destinations
        for i in range(self.zipSize):
            numConn = random.randint(1, maxConnections)
            connList = random.sample(range(0, self.zipSize), numConn)

            # loops through the destinations, and randomly generates the weight, and then assigns the weights in an
            # undirected fashion using both nodes as start and end, only leaving out a connection if the node points to itself
            for j in range(len(connList)):
                if i != connList[j]:
                    weight = random.randint(self.MIN_WEIGHT, self.MAX_WEIGHT)
                    zipMatrix[i][connList[j]] = weight
                    zipMatrix[connList[j]][i] = weight

        # creates the adjacency matrix
        checkMatrix = [[0 for x in range(self.zipSize)] for y in range(self.zipSize)]

        # fills the adjacency matrix, and sets connections to a node equal to 1, and sets the diagonal to 1
        for i in range(self.zipSize):
            for j in range(self.zipSize):
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
            for i in range(self.zipSize):
                zeroFound = False
                # matrix mulitplication step
                connMatrix = copy.deepcopy(self.connectMatrix(connMatrix, checkMatrix, self.zipSize))

            # checks the matrix for a zero, if one is found, it breaks out of the loop
            for j in range(self.zipSize):
                for k in range(self.zipSize):
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

        out.write("source,destination,distance\n")

        for i in range(self.zipSize):
            for j in range(self.zipSize):
                if zipMatrix[i][j] != 0:
                    out.write(str(self.zip[i]) + "," + str(self.zip[j]) + "," + str(zipMatrix[i][j]) + "\n")
        out.close()          

    # https://stackoverflow.com/questions/21547462/how-to-multiply-2-dimensional-arrays-matrix-multiplication
    # the above URL provided the base function for multiplying 2 matricies
    # this function multiplies two square matricies and saves the result in a matrix of the same size
    def connectMatrix(self, connectMatrix, adjMatrix, mSize):
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

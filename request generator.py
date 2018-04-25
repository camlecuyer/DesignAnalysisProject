import random

zip = []

# constants for different vehicles
AMBULANCE = 1
FIRE_TRUCK = 2
POLICE_CAR = 3

# reads in the zipcodes and saves them to zip list
with open('zipcodes.txt','r') as file:
#with open('zipcodesMedTest.txt','r') as file:
    for line in file:
        data = line.rstrip()
        zip.append(data)
file.close()

# gets the number of zipcodes
size = len(zip)

# randomly selects a number between 2 and 5
# the number is then multiplied by the number of zipcodes to determine the number of requests and vehicles
requestNumSize = random.randint(2, 5)
#requestNumSize = 1
requestNum = size * requestNumSize

# totals of each type of vehicle
total_police = 0
total_firetruck = 0
total_ambulance = 0

# outputs the requests and vehicles to separate files
out =  open('requests.csv', 'w')
outV = open('vehicles.csv', 'w')
#out =  open('requestsMedTest.csv', 'w')
#outV = open('vehiclesMedTest.csv', 'w')

# loops through the number of requests, and randomly generates the vehicle required,
# the location of the request, and generates a different location for the vehicle to start at
for i in range(requestNum):
    request = random.randint(0, size - 1)
    vehicleLoc = random.randint(0, size - 1)
    vehicle = random.randint(1,3)

    # increases the total vehicles
    if vehicle == AMBULANCE:
        total_ambulance += 1
    elif vehicle == FIRE_TRUCK:
        total_firetruck += 1
    else:
        total_police += 1

    #print(str(i + 1) + "," + str(vehicle) + "," + zip[request])

    # outputs the results their respective file    
    out.write(str(i + 1) + "," + str(vehicle) + "," + zip[request] + "\n")
    outV.write(str(i + 1) + "," + str(vehicle) + "," + zip[vehicleLoc] + "\n")
out.close()
outV.close()

# outputs the totals to a separate file
out =  open('requestNum.txt', 'w')
#out =  open('requestNumMedTest.txt', 'w')

out.write(str(total_ambulance) + "," + str(total_firetruck) + "," + str(total_police) + "\n")

out.close()

#print(total_police)
#print(total_firetruck)
#print(total_ambulance)

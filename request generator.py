import random

zip = []

AMBULANCE = 1
FIRE_TRUCK = 2
POLICE_CAR = 3

with open('zipcodes.txt','r') as file:
    for line in file:
        data = line.rstrip()
        zip.append(data)
file.close()

size = len(zip)

requestNumSize = random.randint(2, 5)
requestNum = size * requestNumSize

total_police = 0
total_firetruck = 0
total_ambulance = 0

out =  open('requests.csv', 'w')
outV = open('vehicles.csv', 'w')
#randomly choose number of children between 1 and 20% of zip for every node
for i in range(requestNum):
    request = random.randint(0, size - 1)
    vehicleLoc = random.randint(0, size - 1)
    vehicle = random.randint(1,3)

    if vehicle == AMBULANCE:
        total_ambulance += 1
    elif vehicle == FIRE_TRUCK:
        total_firetruck += 1
    else:
        total_police += 1

    #print(str(i + 1) + "," + str(vehicle) + "," + zip[request])
        
    out.write(str(i + 1) + "," + str(vehicle) + "," + zip[request] + "\n")
    outV.write(str(i + 1) + "," + str(vehicle) + "," + zip[vehicleLoc] + "\n")
out.close()
outV.close()

out =  open('requestNum.txt', 'w')

out.write(str(total_ambulance) + "," + str(total_firetruck) + "," + str(total_police) + "\n")

out.close()

print(total_police)
print(total_firetruck)
print(total_ambulance)

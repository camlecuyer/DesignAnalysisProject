import random

# takes in a range of data and samples 50 random zipcodes from that range
data = random.sample(range(64000, 66000), 50)
#data = random.sample(range(64000, 66000), 15)
#print(data)

# sorts the data
data.sort()
#print(data)

# outputs the data to file: zipcodes.txt with end line characters after each zipcode
file =  open('zipcodes.txt', 'w')
#file =  open('zipcodesMedTest.txt', 'w')

for zcode in data:
    file.write(str(zcode) + "\n")

file.close()

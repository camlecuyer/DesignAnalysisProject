import random

data = random.sample(range(64000, 66000), 50)
#print(data)
data.sort()
print(data)

file =  open('zipcodes.txt', 'w')
for zcode in data:
    file.write(str(zcode) + "\n")

file.close()

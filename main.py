import csv
import sys
import Dijkstra
from collections import OrderedDict



graph_file = csv.DictReader(open("graph1.csv"))
#for row in input_file:
  #  print (row)

# save previous node to avoid duplicated data---------------------
previous_node=[]
for edg in graph_file:

    previous_node.append(edg)

    for previous in previous_node:
        if int(edg['source']) == int(previous['destination']) and int(edg['destination']) == int(previous['source']) :
            previous_node.pop()

#print(previous_node)
#do maping ID with zipcode:-----------------------------------------
zipcode_ID={}
ID_zipcode={}
j=0
for i in previous_node:
    if int(i['source']) not in zipcode_ID.values() :
        zipcode_ID[j]=int(i['source'])
        j=j+1
    if int(i['destination']) not in zipcode_ID.values() :
        zipcode_ID[j]=int(i['destination'])
        j= j + 1
#print (zipcode_ID)
# reserve ID and map to use them again in final result:
for k in zipcode_ID:
    value=zipcode_ID[k]
    ID_zipcode[value]=k
#print (ID_zipcode)
#print ('values',zipcode_ID.values())
#--------------------------------------------------------------------

number_of_zipcodes = len(ID_zipcode)
graph = Dijkstra.Graph(number_of_zipcodes)

for i in previous_node:
    source_zipcode = int(i['source'])
    destination_zipcode = int(i['destination'])
    source_id = ID_zipcode[source_zipcode]
    destination_id = ID_zipcode[destination_zipcode]
    distance = int(i['distance'])
    graph.addEdge(source_id, destination_id, distance)
    #graph.addEdge(int(i['i']), int(i['destination']), int(i['distance']))
    #graph.addEdge(int(edg['source']), int(edg['destination']), int(edg['distance']))
    #print(edg['source'], edg['destination'], edg['distance'])

# read csv files for vehicles and request and put them in dictionary:---------------------
vehicles_file= csv.DictReader(open("vehicles_case.csv"))
vehicles=[]
for v in vehicles_file:
    v['availability']= True
    vehicles.append(v)

request_file = csv.DictReader(open("request_cases.csv"))
requests =[]
for r in request_file:
    requests.append(r)
#-------------------------------------------------------------------------------------------------------
for req in requests:

    source = ID_zipcode[int(req['location'])]
    # if the first vehicles is available in the same loction of the request:

    for vec in vehicles:
        if (int(vec['location']) == int(req['location'])) and int(vec['type']) == int(req['type']) and vec[ 'availability'] == True:
            req['vehicle_ID'] = vec['vehicle_ID']
            req['distance'] = 0
            vec['availability'] = False
            req['vehicle_location '] = vec['location']
            print (req)
            break

    if 'vehicle_ID' not in req:
        result = graph.dijkstra(source)

        #print (result)
        result_dict = dict(zip(range(number_of_zipcodes),result))
        result_sorted_dict= OrderedDict(sorted(result_dict.items(), key=lambda x: (-x[1], x[0]), reverse=True))
        #print(result_dict)
        #print(result_sorted_dict)

        current_zipcodeID=0
        current_distance=0
        current_zipcode=0
        for key in result_sorted_dict:
            current_zipcodeID =key
            current_distance =result_sorted_dict[key]
            current_zipcode= zipcode_ID[current_zipcodeID]
            for vec in vehicles:
                if(int(vec['location'])== current_zipcode)and int(vec['type']) == int(req['type']) and vec['availability']== True:
                    req['vehicle_ID']= vec['vehicle_ID']
                    req['distance']=current_distance
                    vec['availability']=False
                    req['vehicle_location ']= vec['location']
                    print (req)
                    break
            # for break for key loop if we assign vehicle to request stop looking for another location:
            if 'vehicle_ID' in req :
                break


#sorted_list = sorted(unsorted_List, key=itemgetter(1))
#print(sorted_list)

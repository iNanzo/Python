#Import Json class library
import json

#Create dictionary array
data1 = {
    "name":"Newton Hoang",
    "age":"24",
    "city":"Seattle",
    "interests":["Dungeons & Dragons", "Video Game Development", "Movies", "Art", "World Bulding"],
    "isStudent":False
}

#####
#with condition that converts data into a json file
with open("data1.json", "w") as json_file:
    json.dump(data1, json_file, indent = 4)

#Confirmation prompt
print("Successfully written to data1.json")

##########
#

with open("data1.json","r") as json_file:

    loaded_data = json.load(json_file)

#Confirmation prompt
print("Successfully read data1.json")
#Data output to terminal
print(loaded_data)

##########
#

loaded_data["age"] = 18
loaded_data["interests"].append("Board Games")
loaded_data["interests"].remove("Art")

##########
#

with open("data1.json", "w") as json_file:
    json.dump(loaded_data, json_file, indent = 4)

#Confirmation prompt
print("Successfully written to data1.json")
print(loaded_data)

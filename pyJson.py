# Import Json class library
import json

# Create dictionary array
data1 = {
    "name":"Newton Hoang",
    "age":"24",
    "city":"Seattle",
    "interests":["Dungeons & Dragons", "Video Game Development", "Movies", "Art", "World Bulding"],
    "isStudent":False
}

#####
# Write the dictionary data into a JSON file with proper formatting
with open("data1.json", "w") as json_file:
    json.dump(data1, json_file, indent = 4)

# Confirmation prompt
print("Successfully written to data1.json")

##########
# Open the JSON file and load its content into a Python object (dictionary)
with open("data1.json","r") as json_file:
    loaded_data = json.load(json_file)

# Confirmation prompt
print("Successfully read data1.json")

# Data output to terminal
print(loaded_data)

##########
# Modify the loaded data1
loaded_data["age"] = 18
loaded_data["interests"].append("Board Games")
loaded_data["interests"].remove("Art")

##########
# Write the modified data back into the JSON file, overwriting the old content
with open("data1.json", "w") as json_file:
    json.dump(loaded_data, json_file, indent = 4)

# Confirmation prompt
print("Successfully written to data1.json")

# Output the updated data to the terminal
print(loaded_data)

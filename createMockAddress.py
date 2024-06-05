import json

# Step 2: Create a dictionary
def writeToJson():
    my_dict = {
            "line1":"3100 S Orange Ave",
            "city": "Orlando",
            "state": "FL",
            "postal_code": "32806",
            "country": "US",
            }

    # Step 3: Open the file in write mode to reset it and write the dictionary to the JSON file
    with open('address.json', 'w') as json_file:
        json.dump(my_dict, json_file)
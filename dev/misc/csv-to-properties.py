import csv
import pprint

properties = []
with open("board-info.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")

    for row in reader:
        property_dict = {}
        for key, value in row.items():
            # Remove everything after the newline character, if present
            if value:
                value = value.split("\n")[0]
            
            # Convert 'NaN' and empty strings to None
            if value == "NaN" or value == "":
                property_dict[key] = None
            # Convert numerical strings to integers or floats
            elif value.isdigit():
                property_dict[key] = int(value)
            elif value.replace(".", "", 1).isdigit():
                property_dict[key] = float(value)
            else:
                property_dict[key] = value
        properties.append(property_dict)

pprint.pprint(properties)

# Write the formatted properties to a Python file
with open("properties.txt", "w") as f:
    f.write("properties = ")
    f.write(pprint.pformat(properties))

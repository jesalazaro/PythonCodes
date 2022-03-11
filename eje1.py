import json

with open("json/data1.json", "r") as read_file:
    data = json.load(read_file)


print(data["nombres"])

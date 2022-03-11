import json

data = {
  "cientifico": {
      "nombre": "Alan Mathison Turing",
      "edad": "41"
      }
  }

with open("json/data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
print(json_string, type(json_string))

json_string = json.dumps(data, indent=4)
print(json_string)


with open("json/data_file.json", "r") as  read_file:
    data = json.load(read_file)

print(data["cientifico"])

json_string = """{"cienfico": {"nombre" : "Alan Mathison Turing", "edad": "41"}}"""
data = json.loads(json_string)
print(data)

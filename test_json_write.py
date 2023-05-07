import json

# Data to be written
dictionary = {
	"time": "20:00:00",
	"session": "study"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)

import json

# data = {"id":1, "name":"aaa"}
# print(type(data))
# json_str = json.dumps(data)
# print(type(json_str))
# print(json_str)

# with open('data.json', 'w') as f:
# 	json.dump(data, f)

with open('data.json', 'r') as f:
	# print(f.read())
	str = json.load(f)
	print(str)
import json

def load_progress():
	try:
		with open('data.json', 'r') as f:
			return json.load(f)
	except:
		return {"completed": []}

def save_progress(data):
	with open('data.json', 'w') as f:
		json.dump(data, f, indent=4)


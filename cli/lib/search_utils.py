import json
def load_dataset():
	with open('data/movies.json', 'r') as file:
		raw_data = json.load(file)
	
	data = {}
	for movie_dict in raw_data["movies"]:
		id, title, description = movie_dict.values()
		data[id] = (title, description)
	return data

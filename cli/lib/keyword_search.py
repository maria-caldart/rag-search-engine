import string

# Load stopwords once
file = open("data/stopwords.txt", 'r')
sw = (file.read()).splitlines()

def tokenization(text):
	tok_text = text.split()
	return tok_text

def stopword_removal(text):
	file = open("data/stopwords.txt", 'r')
	sw = (file.read()).splitlines()
	pre_text = []
	for token in text:
		if token not in sw:
			pre_text.append(token)
	return pre_text

def preprocessing(text):
	# 1. Remove punctuation
	rm_punct_map_table = str.maketrans("", "", string.punctuation)
	pre_text = (text.translate(rm_punct_map_table)).lower()
	# 2. Tokenization
	pre_text = tokenization(pre_text)
	# 3. Stop word removal
	pre_text = stopword_removal(pre_text)
	return pre_text


def find_title_by_query(movies, query):
	results = []
	pre_query = preprocessing(query)
	for id, (title, _) in movies.items():
		pre_title = preprocessing(title)
		found = False
		for query_token in pre_query:
			for title_token in pre_title:
				if query_token in title_token:
					results.append((id, title))
					found = True
					break
			if found:
				break	
	return results

def print_results(results):
	n = min(len(results), 5)
	for i in range(n):
		id, title = results[i]
		print(str(id) + ": " + title)

import string
from nltk.stem import PorterStemmer

# Load stopwords once
with open("data/stopwords.txt", 'r') as f:
	sw = (f.read()).splitlines()

def tokenization(text):
	tok_text = text.split()
	return tok_text

def stopword_removal(text):
	with open("data/stopwords.txt", 'r') as f:
		sw = (f.read()).splitlines()
	
	pre_text = []
	for token in text:
		if token not in sw:
			pre_text.append(token)
	return pre_text

def stemming(text):
	stemmer = PorterStemmer()
	pre_text = []
	for token in text:
		pre_text.append(stemmer.stem(token))
	return pre_text

def preprocessing(text):
	# 1. Remove punctuation
	rm_punct_map_table = str.maketrans("", "", string.punctuation)
	pre_text = (text.translate(rm_punct_map_table)).lower()
	# 2. Tokenization
	pre_text = tokenization(pre_text)
	# 3. Stop word removal
	pre_text = stopword_removal(pre_text)
	# 4. Stemming
	pre_text = stemming(pre_text)
	return pre_text
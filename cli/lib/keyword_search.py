from lib.preprocessing import preprocessing
from lib.search_utils import load_dataset
import pickle
from collections import Counter


def find_title_by_query(inv_index_movies, query):
	results = []
	pre_query = preprocessing(query)
	total_doc_ids = []
	for query_token in pre_query:
		doc_ids = inv_index_movies.get_documents(query_token)
		total_doc_ids += doc_ids
		if len(total_doc_ids) > 5:
			total_doc_ids = total_doc_ids[:5]
			total_doc_ids.sort()
			break
	
	for doc_id in total_doc_ids:
		title = inv_index_movies.get_title(doc_id)
		results.append((doc_id, title))
	return results

def print_results(results):
	n = min(len(results), 5)
	for i in range(n):
		id, title = results[i]
		print(str(id) + ": " + title)

def build_command(inverted_index):
	inverted_index.build()

def load_command(inverted_index):
	inverted_index.load()

def preprocess_one_term(term):
	tok_term = preprocessing(term)
	if len(tok_term) != 1:
		raise Exception("More than one term passed. To check term frecuency only one term must be given.")
	else:
		return tok_term[0] 

class InvertedIndex:
	index = {}
	docmap = {}
	term_frecuencies = {}

	def __add_document(self, doc_id, title, description):
		self.docmap[doc_id] = {"title": title, "description": description}
		tok_text = preprocessing(title) + preprocessing(description)
		self.term_frecuencies[doc_id] = Counter(tok_text)
		for token in tok_text:
			self.index.setdefault(token, []).append(doc_id)

	def get_documents(self, term):
		doc_ids = []
		if term in self.index:
			doc_ids = self.index[term]
		doc_ids.sort()
		return doc_ids

	def get_title(self, doc_id):
		return self.docmap[doc_id]["title"]

	def get_tf(self, doc_id, term):
		if term in self.term_frecuencies[doc_id]:
			return self.term_frecuencies[doc_id][term]
		else: return 0

	def build(self):
		movies = load_dataset()
		for id, (title, description) in movies.items():
			self.__add_document(id, title, description)
		self.save()
		#return self

	def load(self):
		with open("cache/index.pkl", "rb") as f:
			self.index = pickle.load(f)
		with open("cache/docmap.pkl", "rb") as f:
			self.docmap = pickle.load(f)
		with open("cache/term_frecuencies.pkl", "rb") as f:
			self.term_frecuencies = pickle.load(f)
		#return self

	def save(self):
		with open("cache/index.pkl", "wb") as f:
			pickle.dump(self.index, f)
		with open("cache/docmap.pkl", "wb") as f:
			pickle.dump(self.docmap, f)
		with open("cache/term_frecuencies.pkl", "wb") as f:
			pickle.dump(self.term_frecuencies, f)


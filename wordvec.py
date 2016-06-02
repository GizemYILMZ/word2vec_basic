 # import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname
	def __iter__(self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname, fname)):
				yield line.split()

sentences = MySentences('/some/directory') # a memory-friendly 
model = gensim.models.Word2Vec(sentences)

model = Word2Vec(sentences, min_count=10)  # default value is 
model = Word2Vec(sentences, size=200)  # default value is 100
model = Word2Vec(sentences, workers=4) # default = 1 worker = no parallelization


model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)


model.doesnt_match("breakfast cereal dinner lunch".split())
model.similarity('woman', 'man')

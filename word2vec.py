# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


model = gensim.models.Word2Vec.load_word2vec_format('/home/gizem/Python/GoogleNews-vectors-negative300.bin.gz', binary=True)


print model.similarity('woman', 'man') 



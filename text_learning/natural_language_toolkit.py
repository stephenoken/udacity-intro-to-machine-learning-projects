from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
sw = stopwords.words("english")

print len(sw)


stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive") # NOTE: the 'un'

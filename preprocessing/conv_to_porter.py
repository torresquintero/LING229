# takes a CMU dictionary, returns the same corpus
# with porter stems for the words
import sys
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

if len(sys.argv) != 2:
	print("python conv_to_porter.py corpus.txt")

CMU_corpus = sys.argv[1]
old_f = open(CMU_corpus)
new_f = open("porter_cmubh.txt", "w")
for line in old_f:
	if line:
		sent = line.split()
		sent[0] = stemmer.stem(sent[0])
		sent = " ".join(str(word) for word in sent)
		new_f.write(sent)
		new_f.write("\n")

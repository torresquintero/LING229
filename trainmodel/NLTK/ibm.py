import sys
from nltk import IBMModel1
from nltk.translate import AlignedSent
from nltk.translate import Alignment

file = sys.argv[1]


def read_corpus(file_name):
	alignments = []
	f = open(file_name)
	for line in f.readlines():
		pron = []
		alignment = []
		line = line.split(" ")
		if line:
			for word in line:
				if word.isspace():
					pass
				if word[0].isdigit():
					alignment.append(word.replace('\n', ''))
				elif word[0].isupper(): 
					pron.append(word)
			alignments.append((list(line[0]), pron, " ".join(alignment)))
	f.close()
	return alignments

	

align_sents = read_corpus(file)
bitext = []
for alignment in align_sents:
	bitext.append(AlignedSent(alignment[0], alignment[1], Alignment.fromstring(alignment[2])))

model = IBMModel1(bitext, 5)

test_sentence = bitext[2]
print test_sentence.words
print test_sentence.mots
print test_sentence.alignment

#print('{0:.3f}'.format(model.translation_table['a']['AA']))

#print bitext[365]

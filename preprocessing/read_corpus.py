# takes file name for corpus, returns formatted alignments as a list of triples
# in the form (word, pronunciation in ARPABET, alignment)
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

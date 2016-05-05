import sys
import nltk, re, pprint
import conv_to_porter
from nltk import word_tokenize
from os import system
from nltk import PorterStemmer


if len(sys.argv) != 2:
	print("python CMU.py CMU_corpus.txt")

CMU_corpus = "python conv_to_porter.py " + sys.argv[1] + " porter_cmubh.txt"
stemmer = PorterStemmer()
system(CMU_corpus)

# IMP: need to account for morphology in the output!!!
# all the CMU entries are dictionary-style
f = open("porter_cmubh.txt")
pronunciations = {}
for line in f:
	if line:
		sent = line.split()
		word = sent[0]
		length = sent[-1]
		freq_homograph = sent[-2]
		freq = sent[-3]
		# this doesn't account for multiple pronunciations
		# esp for diff. stresses for the same word (separate entries)
		pronunciation = sent[1:-3]
		pronunciations[word] = pronunciation
	
user_word = "random_string_wooooooo"
# the porter stemmed version of 'exit' is 'exit'
while(user_word != "exit"):
	user_word = input("\nGive me a word, and I'll give you its pronunciation!\nType exit to exit the program.\n\n")
	user_word = stemmer.stem(user_word)
	if user_word == "exit":
		exit()
	elif not (user_word in pronunciations.keys()):
		print("\nThat's not in the CMU dictionary. Please try again.")
	else: 
		print(pronunciations[user_word])




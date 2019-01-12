import nltk
from nltk.corpus import cmudict 
d = cmudict.dict() 

sentence = raw_input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
	print(d[word])

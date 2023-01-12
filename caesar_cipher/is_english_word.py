# how to get list of words

# import nltk
import nltk
import re

# download corpus required
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

# now that they download we can import
from nltk.corpus import words, names

# save to useful variables

# all words are lowercase
word_list = words.words()
# all names have first char capital letter
name_list = names.words()

# dats a lot of words!
print(word_list)

def count_words(text):
	word_count = 0
	split_words = text.split()
	for word in split_words:
		word = re.sub(r"[^A-Za-z]+", "", word)
		if word.lower() in word_list or word.title() in name_list:
			word_count += 1
	return word_count


text = "hi my name is, brian"
print(count_words("hi my na,,,,me is, brian")/len(text.split()))

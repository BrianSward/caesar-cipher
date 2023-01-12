# imports
import nltk
import re

# download corpus required
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

# now that they download we can import
from nltk.corpus import words, names

# variables
# NOTE! all words are lowercase
word_list = words.words()
# dats a lot of words!
# print(word_list)
# NOTE! all names have first char capital letter
name_list = names.words()
# alphabet to use for cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plaintext, key):
	"""
	takes in plain text and a key, returns encrypted cipher text
	"""
	c_text = ""
	for char in plaintext:
		if char.isalpha():
			if char.isupper():
				place = alphabet.index(char.lower())
				new_place = (place + key) % len(alphabet)
				new_letter = alphabet[new_place]
				c_text += new_letter.upper()
			else:
				place = alphabet.index(char.lower())
				new_place = (place + key) % len(alphabet)
				new_letter = alphabet[new_place]
				c_text += new_letter
		else:
			c_text += char

	return c_text


def decrypt(plaintext, key):
	"""
	takes in plain text and a key, returns decrypted cipher text
	"""
	c_text = ""
	for char in plaintext:
		if char.isalpha():
			if char.isupper():
				place = alphabet.index(char.lower())
				new_place = (place - key) % len(alphabet)
				new_letter = alphabet[new_place]
				c_text += new_letter.upper()
			else:
				place = alphabet.index(char.lower())
				new_place = (place - key) % len(alphabet)
				new_letter = alphabet[new_place]
				c_text += new_letter
		else:
			c_text += char

	return c_text


def count_words(text):
	"""
	helper function which takes in a string an counts words for us
	"""
	word_count = 0
	split_words = text.split()
	for word in split_words:
		word = re.sub(r"[^A-Za-z]+", "", word)
		if word.lower() in word_list or word.title() in name_list:
			word_count += 1
	return word_count


def crack(plaintext):
	"""
	function which takes in encrypted text and returns the best possible matching crack
	"""
	results = []
	for x in range(len(alphabet)):
		c_text = ""
		for char in plaintext:
			if char.isalpha():
				if char.isupper():
					place = alphabet.index(char.lower())
					new_place = (place - x) % len(alphabet)
					new_letter = alphabet[new_place]
					c_text += new_letter.upper()
				else:
					place = alphabet.index(char.lower())
					new_place = (place - x) % len(alphabet)
					new_letter = alphabet[new_place]
					c_text += new_letter
			else:
				c_text += char
		results.append((x, count_words(c_text) / len(plaintext.split())))
	max_ = (0, 0)
	for result in results:
		if result[1] > float(max_[1]):
			max_ = result
	if max_[1] < .40:
		return ""
	else:
		return decrypt(plaintext, max_[0])

if __name__ == '__main__':
	print(crack("vw am boas wg, pfwob"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plaintext, key):
	c_text = ""
	for char in plaintext:
		# cast string into integer
		num = int(char)
		num = (num + key) % 10
		c_text += str(num)

	return c_text


def decrypt(plaintext, key):
	c_text = ""
	for char in plaintext:
		# cast string into integer
		num = int(char)
		num = (num - key) % 10
		c_text += str(num)

	return c_text


print(encrypt("937", 5))
print(decrypt("482", 5))

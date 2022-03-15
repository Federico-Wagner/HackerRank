"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of
the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
"""

def caesarCipher(s, k):
	# Write your code here
	if k > 26:
		k = k % 26
	lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			  'v', 'w', 'x', 'y', 'z'] * 2
	uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
			  'V', 'W', 'X', 'Y', 'Z'] * 2
	def convert_letter(letter):
		if (letter not in lowers and letter not in uppers):
			return letter
		else:
			if letter in lowers:
				return lowers[lowers.index(letter) + k]
			if letter in uppers:
				return uppers[uppers.index(letter) + k]
	output = ""
	for letter in s:
		output += convert_letter(letter)

	return output
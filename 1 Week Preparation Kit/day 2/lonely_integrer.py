"""Given an array of integers, where all elements but one occur twice, find the unique element."""

def lonelyinteger(a):
	# Write your code here
	print(set(a))
	for numbers in set(a):
		count = 0
		for number in a:
			if number == numbers:
				count += 1

		if count == 1:
			return numbers
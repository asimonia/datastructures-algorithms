from pythonds.basic.stack import Stack

def divideBy2(decNumber):
	"""Takes decimal number (base 10) and returns a binary
	representation (base 2)
	"""
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ''
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n, base):
	"""
	Returns a string representation of a number in base from n.
	"""
	convertString = "0123456789ABCDEF"
	while n > 0:
		if n < base:
			rStack.push(convertString[n])
		else:
			rStack.push(convertString[n % base])
		n = n // base
	res = ""
	while not rStack.isEmpty():
		res = res + str(rStack.pop())
	return res

def listsum(numList):
	theSum = 0
	for i in numList:
		theSum = theSum + i
	return theSum

def listsum2(numList):
	"""Recurisve version of listsum"""
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listsum2(numList[1:])


"""
A recursive algorithm must have a base case.
A recursive algorithm must change its state and move toward the base case.
A recursive algorithm must call itself, recursively.
"""
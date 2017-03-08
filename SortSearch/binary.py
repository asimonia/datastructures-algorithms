def binarySearch(alist, item):
	"""
	[4, 6, 10, 14, 19, 25, 60]

	first = 0
	last = 6
	
	The list must be ordered.
	Check the midpoint for the value in the
	list and compare it to the item.
	Divide and conquer.
	"""
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found


def recursive_binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist[:midpoint], item)
			else:
				return binarySearch(alist[midpoint + 1:], item)

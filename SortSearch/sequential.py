def sequentialSearch(alist, item):
	"""
	
	[0] [1] [2] [3] [4] [5] [6] ...
	Start at position 0 check the first index
	to see if the item is found.  If it is
	found, then True.  If not, then go to the
	next position in the sequence.

	"""
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos = pos + 1

	return found


def orderedSequentialSearch(alist, item):
	"""
	There is an added benefit to performing a sequential search on
	an ordered list for time complexity.  We loop through the list 
	and if the number is not found at the index, we compare the item 
	to the number at the index.  If the item is greater than the number 
	at the index, we know the item is not present.  We terminate the loop.

	a sequential search is improved by ordering the list only in the case 
	where we do not find the item.
	"""
	pos = 0
	found = False
	stop = False
	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos = pos + 1

	return found


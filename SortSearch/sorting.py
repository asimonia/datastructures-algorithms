def bubbleSort(alist):
	"""
	Bubble sort makes multiple passes through a list.
	It compares adjacent items and exchanges those that are out of order.
	Each pass through the list places the next largest value in its proper place.
	"""
	for passnum in range(len(alist) - 1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i + 1]:
				temp = alist[i]
				alist[i] = alist[i + 1]
				alist[i + 1] = temp


def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist) - 1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i] > alist[i + 1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i + 1]
				alist[i + 1] = temp
		passnum = passnum - 1


def selectionSort(alist):
	"""
	Selection sort improves on the bubble sort by making only one exchange
	for every pass through the list.  Looks for the largest value
	as it makes a pass and places it in the proper location.
	"""	
	for fillslot in range(len(alist) - 1, 0, -1):
		positionOfMax=0
		for location in range(1, fillslot + 1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp


def insertionSort(alist):
	"""
	The insertion sort, although still O(n^2), works in a slightly 
	different way. It always maintains a sorted sublist in the lower 
	positions of the list. Each new item is then “inserted” back into 
	the previous sublist such that the sorted sublist is one item larger.
	"""
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentvalue

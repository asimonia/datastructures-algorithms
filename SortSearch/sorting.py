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

"""
A data structure that can be searched in O(1) time.

Hash table is a collection of items stored that makes
them easy to find them later.

Each position on the hash table, often called a slot,
can hold an item and is named by an integer value 
starting at 0.

Hash function - the mapping between an item and the
slot where the item belongs.

Once hash values are determined, we can insert them
into the hash table.  Load factor = (# of items / tablesize).

If the same value is produced for two items and they
try to occupy the same slot, then there is a "collision".

Given a collection of items, a hash function that maps each
item into a unique slot is referred to as a perfect has function.

Goal: create a hash function that:
a) minimizes the # of collisions
b) easy to compute
c) evenly distributes the items in the hash table

folding method: divy up the # into pairs and then sum them together
the result % slots is the slot.
mid-square: square the #, extract two digits and perform the remainder.
"""
def hash(astring, tablesize):
	sum = 0
	for pos in range(len(astring)):
		sum = sum + ord(astring[pos])

	return sum % tablesize
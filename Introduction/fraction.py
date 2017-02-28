"""
Implement the abstract data type Fraction as a class.
"""

def gcd(m, n):
	"""Helper function to find the greatest common denominator"""
	while m % n != 0:
		oldm = m
		oldn = n
		m = oldn
		n = oldm % oldn
	return n


class Fraction:

	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def __add__(self, otherfraction):
		newnum = self.num * otherfraction.den + self.den * otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __str__(self):
		return '{num}/{den}'.format(num=self.num, den=self.den)


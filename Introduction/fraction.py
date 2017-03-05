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
		"""Initialize a fraction with a numerator and denominator"""
		self.num = top
		self.den = bottom

	def __add__(self, otherfraction):
		"""Override the add operator
		Cross multiply.
		Use the product of the two denominators as the common denominator.
		Find the greatest common denominator to simply
		the denominator and return the result.
		"""
		newnum = self.num * otherfraction.den + self.den * otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __str__(self):
		"""Print out the fraction so it looks like 3/5"""
		if self.den == 1:
			return '{num}'.format(num=self.num)
		else:
			return '{num}/{den}'.format(num=self.num, den=self.den)

	def __eq__(self, other):
		"""Deep equality is equality by the same value, not by the same reference."""
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __mul__(self, other):
		"""Multiply"""
		newnum = self.num * other.num
		newden = self.den * other.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __sub__(self, other):
		"""Subtract"""
		newnum = self.num * other.den - self.den * other.num
		newden = self.den * other.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __div__(self, other):
		"""Division"""
		newnum = self.num * other.den
		newden = self.den * other.num
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)

	def __lt__(self, other):
		"""Perform less than operation
		   Returns boolean
		"""
		num1 = self.num / self.den
		num2 = other.num / other.den
		return num1 < num2

	def __gt__(self, other):
		"""Perform greater than operation
		   Returns boolean
		"""
		num1 = self.num / self.den
		num2 = other.num / other.den
		return num1 > num2


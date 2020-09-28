## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	'''
	compute the lowest term of a fraction
	:param x: string containing a fraction
	:return: reduce form of x
	'''

	def greatest_common_divisor(n, d):
		'''
		find the largest factor divisible by n and d
		:param n: integer
		:param d: integer
		:return: return the greatest common factor of n and d
		'''

		while d !=0:
			temp = d
			d = n%d
			n = temp

		return n

	numerator, denominator = map(int, x.split('/'))

	#checking for 'undefined' and numerator of zero
	if numerator == 0:
		result = '0'
	elif denominator == 0:
		result = 'Undefined'
	else:
		greatest = greatest_common_divisor(numerator, denominator)
		numerator /= greatest
		denominator /= greatest

		result = "{}/{}".format(int(numerator),int(denominator))

	return result

print(lowest_terms('20/10'))
print(lowest_terms('16/28'))
print(lowest_terms('-50/25'))
print(lowest_terms('20/-60'))
print(lowest_terms('-300/165'))
print(lowest_terms('-12/-26'))
print(lowest_terms('0/26'))
print(lowest_terms('12/0'))

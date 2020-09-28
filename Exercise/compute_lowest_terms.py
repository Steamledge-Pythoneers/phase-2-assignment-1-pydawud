## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	'''
	compute the lowest term of a fraction
	:param x: string containing a fraction
	:return: reduce form of x
	'''
	numerator, denominator = map(int, x.split('/'))
	def greatest_common_divisor(n, d):
		while d !=0:
			temp = d
			d = n%d
			n = temp

		return n
	greatest = greatest_common_divisor(numerator, denominator)
	numerator /= greatest
	denominator /= greatest

	#print(numerator,denominator)
	return "{}/{}".format(int(numerator),int(denominator))

#lowest_terms('20/10')
print(lowest_terms('20/10'))
print(lowest_terms('16/28'))
print(lowest_terms('-50/25'))
print(lowest_terms('20/-60'))
print(lowest_terms('-300/165'))
print(lowest_terms('-12/-26'))

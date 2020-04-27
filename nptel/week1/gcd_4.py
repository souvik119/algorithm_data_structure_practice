#!/usr/bin/env python3

def gcd(m,n):
	'''Further improvements:
	1. Why go from front. If we start from end, first factor we find is GCD
	2. No need to store value, return it directly and exit the function then and there'''
	i = min(m,n)
	while i > 0:
		if m%i == 0 and n%i == 0:
			return i
		else:
			i = i - 1

print(gcd(14, 63))
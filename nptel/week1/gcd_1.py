#!/usr/bin/env python3


def gcd(m,n):
	'''Returns greatest common divisor of m, n. Steps for doing the same are as below:
	1. Calculate and store factors of m in a list fm
	2. Calculate and store factors of n in a list fn
	3. For each item in fm check if same element is in fn, is so append to list cf
	4. Return greatest item in cf (rightmost)'''
	fm = [] #factors of m
	for i in range(1, m+1):
		if m % i == 0:
			fm.append(i)

	fn = [] #factors of n
	for i in range(1, n+1):
		if n % i == 0:
			fn.append(i)

	cf = [] #common factors
	for i in fm:
		if i in fn:
			cf.append(i)

	return cf[-1]

print(gcd(14, 63))
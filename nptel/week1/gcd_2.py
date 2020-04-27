#!/usr/bin/env python3

def gcd(m,n):
	'''Few improvements related to original algorithm:
	1. Make a single pass from 1 to min(m,n)
	2. Only 1 list this time and factors appended if they divide both m, n'''
	cf = []
	for i in range(1, min(m,n)+1):
		if m%i == 0 and n%i == 0:
			cf.append(i)

	return cf[-1]

print(gcd(14, 63))
#!/usr/bin/env python3

def gcd(m,n):
	'''Further improvements:
	1. Dont need list
	2. Single valriable can be updated each time we encounter new gcd'''
	for i in range(1, min(m,n)+1):
		if m%i == 0 and n%i == 0:
			cf = i

	return cf

print(gcd(14, 63))
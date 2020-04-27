#!/usr/bin/env python3

def gcd_recursive(m,n):
	'''Better version of this algo:
	1. If n divides m, return n
	2. r = m%n
	3. return gcd(n,r)'''
	if m < n:
		#exchange values
		m,n = n,m 

	if m%n == 0:
		return n

	else:
		rem = m%n
		return gcd_recursive(n, rem)


def gcd_while(m,n):
	'''While loop version of the same algo'''
	if m < n:
		#exchange values
		m,n = n,m

	while m%n != 0:
		rem = m%n
		m,n = n,rem

	return n


print(gcd_recursive(14, 63))
print(gcd_while(14, 63))
#!/usr/bin/env python3

def gcd_recursive(m,n):
	'''Recursive version of Euclid's algo for GCD (assuming m > n):
	1. If n divides m, return n
	2. Else, Compute GCD(n, m-n)'''
	if m < n:
		#exchange values
		m,n = n,m 

	if m%n == 0:
		return n

	else:
		diff = m - n
		return gcd_recursive(max(n, diff), min(n, diff))



def gcd_while(m,n):
	'''While loop version of the same algo'''
	if m < n:
		#exchange values
		m,n = n,m

	while m%n != 0:
		diff = m - n
		m,n = max(n,diff), min(n,diff)

	return n


print(gcd_recursive(14, 63))
print(gcd_while(14, 63))
#!/usr/bin/env python3

def binary_search(seq, val, l, r):
	'''Implements binary search algorithm on a sorted list.
	Retruns True is val is present in seq, otherwise returns False'''
	if r-l == 0:
		return False
	mid = (l + r) // 2
	if seq[mid] == val:
		return True

	if val < seq[mid]:
		return binary_search(seq, val, l, mid)
	else:
		return binary_search(seq, val, mid+1, r)


print(binary_search(list(range(100)), 100, 0, len(range(100))))
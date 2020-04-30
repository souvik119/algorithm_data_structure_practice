#!/usr/bin/env python3

def quickSort(seq, l, r):
	'''This sorting technique first assumes a median and then arranges the sequence such that all the smaller numbers are on lhs and 
	larger numbers are on rhs'''
	if r - l <= 1:
		return seq

	#partition wrt pivot element
	smaller_ptr = l+1
	for unknown_ptr in range(l+1, r):
		if seq[unknown_ptr] <= seq[l]:
			seq[smaller_ptr], seq[unknown_ptr] = seq[unknown_ptr], seq[smaller_ptr]
			smaller_ptr = smaller_ptr + 1

	seq[l], seq[smaller_ptr-1] = seq[smaller_ptr-1], seq[l]

	quickSort(seq, l, smaller_ptr-1)
	quickSort(seq, smaller_ptr, r)
	return seq

a = list(range(500,0,-1))
print(quickSort(a, 0, len(a)))

#!/usr/bin/env python3

def InsetionSort(seq):
	'''Returns sorted sequence using Insertion sort method on a unsorted list.
	Ascending order in this case'''
	for index in range(len(seq)):
		pos = index
		while pos > 0 and seq[pos] < seq[pos-1]:
			seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
			pos = pos-1

	return seq

print(InsetionSort([23, 46, 1, 75, 75, 68, 98, 36]))
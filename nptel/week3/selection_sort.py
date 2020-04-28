#!/usr/bin/env python3

def SelectionSort(seq):
	'''Performs selection sort on the unsorted sequence. Ascending order in this case.'''
	for index in range(len(seq)):
		minValueIndex = index #assume starting index in each scan has least value
		for i in range(index, len(seq)):
			if seq[i] < seq[minValueIndex]:
				minValueIndex = i
		seq[index], seq[minValueIndex] = seq[minValueIndex], seq[index] #exchange elements

	return seq

print(SelectionSort([23, 46, 1, 75, 75, 68, 98, 36]))


#!/usr/bin/env python3

def merge(l1, l2):
	'''Performs merge operation to create a sorted list l3 upon recieving 2 sorted lists l1, l2'''
	l3 = [] #initialize l3
	i, j = 0, 0 #keep track of how many indexes covered so far in l1 and l2
	m , n = len(l1), len(l2)
	while i+j < m+n:
		if i == m: #l1  in is done all reamining are in l2
			l3.append(l2[j])
			j = j+1
		elif j == n: #l2  in is done all reamining are in l1
			l3.append(l1[i])
			i = i+1
		elif l1[i] <= l2[j]: #l1 element smaller than l2
			l3.append(l1[i])
			i = i+1
		elif l1[i] > l2[j]: #l2 element smaller than l1
			l3.append(l2[j])
			j = j+1

	return l3

# a = list(range(0,100,2))
# b = list(range(1,75,2))

# print(merge(a, b))

def mergeSort(seq, l, r):
	'''Repeatedly splits the seq into halves based on values of left(l) and right(r) arguments.
	Calls merge function to merge the split sorted lists'''
	if r-l <= 1: #base case: only single item in a list or no items
		return seq[l:r] # make sure to return only that part of the list and not the whole list
	if r-l > 1:
		mid = (l+r) // 2
		L = mergeSort(seq, l, mid)
		R = mergeSort(seq, mid, r)

		return merge(L,R)

a = list(range(1,100,2)) + list(range(0,100,2))
print(mergeSort(a, 0, len(a)))


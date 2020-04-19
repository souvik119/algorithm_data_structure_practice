#!/usr/bin/env python3

class Stack:
	'''This Stack implementation uses list as the primitive data type to implement stack functionality.
	In this case end of list is considered "top" of stack and zeroeth element considered as base'''

	def __init__(self):
		'''Initializes an empty list as starting point of stack'''
		self.items = []

	def isEmpty(self):
		'''Returns True is list is empty otherwise returns False'''
		return self.items == []

	def push(self, item):
		'''Pushes new item at top of stack'''
		self.items.append(item)

	def pop(self):
		'''Deletes element from top pf stack and retuns the deleted element'''
		return self.items.pop()

	def peek(self):
		'''Returns element at top of the stack'''
		return self.items[-1]

	def size(self):
		'''Returns size of stack'''
		return len(self.items)


#!/usr/bin/env python3

class Queue:
	'''This queue implementation uses list data structure. 0th position considered rear of the queue where new items are inserted. Last index of list is considered front of queue where deletions are made.'''
	def __init__(self):
		'''Initializes empty queue'''
		self.items = []

	def isEmpty(self):
		'''Returns true if queue is empty'''
		return self.items == []	

	def enqueue(self, item):
		'''Inserts new item to end of queue (0th position in this implementation)'''
		self.items.insert(0, item)

	def dequeue(self):
		'''Deletes and returns item from the from of queue (last index of list in this implementation)'''
		return self.items.pop()

	def size(self):
		'''Returns length of queue'''
		return len(self.items)
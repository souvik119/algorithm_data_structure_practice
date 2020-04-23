#!/usr/bin/env python3

class Node:
	'''This is a basic building block of a linked list'''
	def __init__(self, node_data):
		''' A node has 2 pieces of info - data and link to next node.
		When creating a new node next link is None because considered end item of the list'''
		self.data = node_data
		self.next = None

	def getData(self):
		'''Returns data of the node'''
		return self.data

	def getNext(self):
		'''Returns link to next Node'''
		return self.next

	def setData(self, newData):
		'''Change value of new node with new data'''
		self.data = newData

	def setNext(self, newNext):
		'''Change next node link'''
		self.next = newNext


class UnrderedList:
	'''Created an unordered linked list using Node class as building blocks'''
	def __init__(self):
		'''Initializes an empty list by pointing head to None'''
		self.head = None

	def isEmpty(self):
		'''Returns true if list is empty'''
		return self.head == None

	def add(self, item):
		'''Adds new node to the list'''
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		'''Returns size of list'''
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()

	def search(self, item):
		'''Returns True if item is in the list'''
		current = self.head
		found = False
		while current != None and not found:
			if item == current.getData():
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		'''Removes item from the list. This implementation assumes item in present the list'''
		current = self.head
		previous = None
		found = False
		while not True:
			if current.getData == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		#if the item is first element of the list
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		'''Inserts new element at the end of list'''
		current = self.head
		while current.getNext() != None:
			current = current.getNext()
		temp = Node(item)
		temp.setNext(current.getNext())
		current.setNext(temp)

	def getIndex(self, item):
		'''Returns index of the item in the list, assuming index starts from 0'''
		current = self.head
		index = 0
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				index += 1
				current = current.getNext()
		return index

	def getItem(self, index):
		'''Returns item in the given index, assumes item is present and index is in range'''
		current = self.head
		for i in range(index):
			current = current.getNext()

		return current.getData()

	def pop(self, index):
		'''Removes the element from list and returns the element'''
		item = self.getItem(index)
		self.remove(item)
		return item

	def insert(self, index, item):
		'''Inserts element at specific position in the list'''
		current = self.head
		for i in range(index):
			current = current.getNext()

		temp = Node(item)
		temp.setNext(current.getNext())
		current.setNext(temp)

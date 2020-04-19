#!/usr/bin/env python3

import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
	'''Basic unittests for class Queue in queue.py module'''
	def setUp(self):
		self.q = Queue()

	def test_1(self):
		self.q.enqueue('hello')
		self.q.enqueue('dog')
		self.q.enqueue(3)
		self.assertEqual('hello', self.q.dequeue())


if __name__ == '__main__':
	unittest.main()
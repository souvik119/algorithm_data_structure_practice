#!/usr/bin/env python3

import unittest
from dequeue import Dequeue

class TestDequeue(unittest.TestCase):

	def setUp(self):
		self.d = Dequeue()

	def test_1(self):
		self.d.addRear('dog')
		self.d.addFront('cat')
		self.d.addFront(True)
		self.assertEqual(3, self.d.size())


if __name__ == '__main__':
	unittest.main()
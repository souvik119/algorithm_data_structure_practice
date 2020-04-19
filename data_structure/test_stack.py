#!/usr/bin/env python3

#naming convention of unittest file is test_<module_name>.py. Following that this file is named test_stack.py
#good practice to keep test file and module in the same library in this case the files are stack.py and test_stack.py

import unittest
from stack import Stack #from <module> import <class_name>

class TestStack(unittest.TestCase): #good practice to use camel casing in terms of Test<class_to_be_tested>(unittest.TestCase)
	def setUp(self):
		'''This method is run before each test case. In this case setting up an instance of class Stack''' 
		self.s = Stack()

	def test_1(self):
		'''All the test cases start with test_ convention'''
		self.s.push('x')
		self.s.push('y')
		self.s.pop()
		self.s.push('z')
		self.assertEqual('z', self.s.peek())

	def test_2(self):
		self.assertEqual(0, self.s.size())

if __name__ == '__main__':
    unittest.main()
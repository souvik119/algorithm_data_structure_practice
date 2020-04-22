#!/usr/bin/env python3

from dequeue import Dequeue

def palchecker(string):
	pal_dq = Dequeue()
	for letter in string:
		pal_dq.addRear(letter)

	flag = True
	while pal_dq.size() > 1 and flag:
		first_char = pal_dq.removeFront()
		last_char = pal_dq.removeRear()
		if first_char != last_char:
			flag = False

	return flag

print(palchecker('lsdkjfskf'))
print(palchecker('radar'))
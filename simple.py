#!/bin/bash

for i in range(1, 405):
	if (i%3 == 0):
		if (i%5 == 0):
			print("FooBar")
		else:
			print("Foo")
	elif (i%5 == 0):
		print("Bar")
	else:
		print(str(i))
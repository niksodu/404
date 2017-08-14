#!/bin/bash

three = 0
five = 0

for i in range(1, 405):
	three += 1
	five += 1

	out = ""
	if (three == 3):
		out = "Foo"
		three = 0
	if (five == 5):
		out += "Bar"
		five = 0

	if (out):
		print(out)
	else:
		print(str(i))
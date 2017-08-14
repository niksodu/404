#!/bin/bash

for i in range(1, 405):
	out = ""
	if (i%3 == 0):
		out = "Foo"
	if (i%5 == 0):
		out += "Bar"

	if (out):
		print(out)
	else:
		print(str(i))
#!/bin/bash

pattern = ["FooBar", None, None, "Foo", None, "Bar", "Foo", None, None, "Foo", "Bar", None, "Foo", None, None]

for i in range(1, 405):
	pat = pattern[i%len(pattern)]
	if (pat):
		print(pat)
	else:
		print(str(i)
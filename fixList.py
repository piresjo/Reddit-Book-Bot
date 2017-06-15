# Get values from text file, remove repeats
# sort, clear text file, and fill with sorted
# values

import re
import os

with open("books.txt", "r") as file:
	bookVal = file.read()
	bookVal = bookVal.split("\n")
	bookVal = list(filter(None, bookVal))

bookValSet = set(bookVal)
bookVal = list(bookValSet)

bookVal = sorted(bookVal, key=str.lower)

open("books.txt", "w").close()

with open("books.txt", "w") as file:
	for title in bookVal:
		file.write(title + "\n")

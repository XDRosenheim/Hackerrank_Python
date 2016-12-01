#!/bin/python3

n = int(input().strip())

text = ""

for i in range(n):
	for j in range(n - i - 1):
		text += " "
	for j in range(i + 1):
		text += "#"
	print(text)
	text = ""

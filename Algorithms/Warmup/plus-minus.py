#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positives = 0
negatives = 0
zeros = 0

for i in range(n):
	if arr[i] > 0:
		positives += 1
	elif arr[i] == 0:
		zeros += 1
	else:
		negatives += 1

print(positives / n)
print(negatives / n)
print(zeros / n)

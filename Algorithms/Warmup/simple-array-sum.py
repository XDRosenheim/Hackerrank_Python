#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
newSum = 0
for i in range(n):
	newSum += arr[i]

print(newSum)

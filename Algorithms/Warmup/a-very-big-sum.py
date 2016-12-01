#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

bigSum = 0

for i in range(n):
	bigSum += arr[i]

print( bigSum )

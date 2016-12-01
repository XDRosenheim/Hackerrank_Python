#!/bin/python

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

total = sum(arr)
print(total - max(arr), total - min(arr))

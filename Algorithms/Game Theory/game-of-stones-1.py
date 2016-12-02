#!/bin/bash
# Get input
t = int(input().strip())

# Run script t times and print winner
for i in range(t):
	stones = input().strip()
	if int(stones) % 7 == 1 or int(stones) % 7 == 0:
		print("Second")
	else:
		print("First")

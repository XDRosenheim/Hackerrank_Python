#!/bin/python3

n = int(input().strip())
a = []
for a_i in range(n):
	a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
	a.append(a_t)

primary = 0

for i in range(n):
	primary += a[i][i]

secondary = 0

for i in range(n):
	secondary += a[i][n - i - 1]

print(abs(primary - secondary))

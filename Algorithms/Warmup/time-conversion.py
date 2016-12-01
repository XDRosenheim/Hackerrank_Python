#!/bin/python3

time = input().strip()

if time[8:9] == "P":
	temptime = int(time[:2]) + 12
	if temptime == 24:
		print(time[:8])
	else:
		print(str(temptime) + time[2:8])
else:
	if int(time[:2]) == 12:
		print("00" + time[2:8])
	else:
		print(time[:8])

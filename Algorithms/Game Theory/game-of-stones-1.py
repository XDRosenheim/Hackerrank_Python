#!/bin/bash
# Get input
t = int(input().strip())
# Make an array and append with input from Hackerrank
arr = []
for i in range(t):
	arr.append(int(input().strip()))

def switchTurn(current):
	if current == 1:
		return 2
	else:
		return 1
	
# Run script t times and print winner
for i in range(t):
	winner = 0  # Reset winner to nothing
	stones = arr[i]  # Amount of stone to play with
	turn = 1  # Set turn holder to player one.
	while winner == 0:
		if stones == 1 and winner == 0:
			winner =
			
	
	if winner == 1:
		print("First")  # Player one wins
	else:
		print("Second")  # Player two wins

"""
Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.
The rules of the game are as follows:

Initially there are n towers.
Each tower is of height m.
The players move in alternating turns.
In each turn, a player can choose a tower of height x and reduce its height to y, where 1<y<x  and y evenly divides x.
If the current player is unable to make a move, they lose the game.
Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.
"""

def towerBreakers(n, m):
	# Write your code here
	towers = [m] * n
	selected_tower = 0
	turn = 0
	while (sum(towers) != len(towers)):

		print(towers)
		if towers[selected_tower] == 1:
			selected_tower += 1
			if selected_tower > n - 1:
				# game ended
				break
		if (towers[selected_tower] != 1 and towers[selected_tower] % 2 == 0):
			if selected_tower == n - 1:
				# take all tower peaces
				towers[selected_tower] = 1
			else:
				# cut in half play
				towers[selected_tower] = towers[selected_tower] // 2
		turn += 1

	if turn % 2 == 0:
		player = "P1"
	else:
		player = "P2"
	print(towers)
	if player == "P1":
		return 2
	else:
		return 1


def towerBreakers2(n, m):
    # Write your code here
    if (m == 1 or n % 2 == 0):
        return 2
    else:
        return 1
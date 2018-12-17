# Impliment Tic Tac Toe 
# Non graphical
# For use in Monte Carlo Tree Search research
# Chris Crisson

import sys

# Initialize the game board
board = [[0,0,0], [0,0,0],[0,0,0]]

# If a win condition is detected, returns player number
# Returns 0 when no win condition is found
def checkWin():
	# Check for row or column win condition
	for i in range(0,3):
		# Make sure a player has played in the spot before 
		# we bother checking the row
		if (board[i][0] > 0):
			# Check ROW where row = i
			if(board[i][0] == board[i][1] and board[i][0] == board[i][2]):
				return board[i][0]
			# Check COLUMN where column = i
			if(board[0][i] == board[1][i] and board[0][i] == board[2][i]):
				return board[0][i]
	# Check for diagonal win condition 
	# Index [1][1] is common so check that it's not 0
	if(board[1][1] > 0):
		# Top left to bottom right
		if(board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
			return board[1][1]
		# Bottom left to top right
		if(board[2][0] == board[1][1] and board[1][1] == board[0][2]) :
			return board[1][1]
	# No win condition detected 
	return 0

# Displays the game board
def displayBoard():
	print(str(board[0][0]) + " | " + str(board[0][1]) + 
		" | " + str(board[0][2]))
	print("_________")
	print(str(board[1][0]) + " | " + str(board[1][1]) + 
		" | " + str(board[1][2]))
	print("_________")
	print(str(board[2][0]) + " | " + str(board[2][1]) + 
		" | " + str(board[2][2]))

# Makes sure input between 0 - 2
# querry is a string that gets passed to raw_input(querry)
# Returns the input
def validateRowOrCol(querry):
	flag = True;
	while flag == True :
		x = raw_input(querry)
		if (int(x) < 0) or (int(x) > 2) :
			print("Enter a number 0 - 2")
		else:
			flag = False
	return x

# Check if move is legal - Space is empty
def validateMove(row, col):
	if board[row][col] == 0:
		return 1
	else: 
		print("That space is ocupied, Pick another")
		return -1

def main():
	# Initialize variable to keep track of whos turn it is
	turn = 0

	# Game Loop
	while checkWin() < 1 :
		turn += 1
		# After 9 turns the board is full so its a tie
		if turn > 9 :
			break
		print("Turn: " + str(turn))
		player = ((turn + 1) % 2) + 1
		displayBoard()
		print("Player " + str(player) + " where do you want to move?")
		flag = True
		while flag == True:
			row = int(validateRowOrCol("Row? "))
			col = int(validateRowOrCol("Col? "))
			if validateMove(row, col) == 1:
				board[int(row)][int(col)] = player
				flag = False

	# Display winner
	winner = checkWin()
	displayBoard()
	if winner > 0 :
		print("Player " + str(winner) + " wins")
	else :
		print("It's a tie")

if __name__ == "__main__":
	main()
	sys.exit()
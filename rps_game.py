# Two player game of rock, paper scissors

# Create dictionary to define which move beats what
# Rock beats scissors
# Paper beats rock
# Scissors beats paper
movesDict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# Keep some statistics
p1WinCount = 0
p2WinCount = 0
tieCount = 0

playAgain = True
while playAgain is True:
    # Get first player's choice
    p1Choice = input("Player 1 GO (rock/paper/scissors): ")
    p2Choice = input("Player 2 GO (rock/paper/scissors): ")

    # Determine the winner
    if movesDict.get(p1Choice) == p2Choice:
        print("Player one wins!")
        p1WinCount += 1
    elif p1Choice == p2Choice:
        print("Tie!")
        tieCount += 1
    else:
        print("Player two wins!")
        p2WinCount += 1

    # Ask if they want to play again
    resp = input('Play again? (y/n)')
    if resp == 'n' or resp == 'N':
        print(resp)
        playAgain = False

# Display the game statistics
print("Player 1 win count:" + str(p1WinCount) + "\nPlayer 2 win count:" + str(p2WinCount) + "\nTie count:" + str(tieCount))
class Player():

    def __init__(self, name):
        self.name = name
        self.winCount = 0
        self.moveHistory = []

    def requestMove(self):
        newMove = input(self.name + " What is your move?")
        self.saveMove(newMove)

    # Maintain a history of moves
    def saveMove(self, newMove):
        self.moveHistory.append(newMove)

    def incrementWinCount(self):
        self.winCount += 1

    def getName(self):
        return self.name

    def getWinCount(self):
        return self.winCount

    def getLastMove(self):
        print(str(self.moveHistory[-1]))
        return self.moveHistory[-1]


# Two player game of rock, paper scissors
player1 = Player("Tyler")
player2 = Player("Kaitlin")

# Create dictionary to define which move beats what
# Rock beats scissors
# Paper beats rock
# Scissors beats paper
movesDict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

playAgain = True
while playAgain is True:
    # Get first player's move
    player1.requestMove()
    # Get the second player's move
    player2.requestMove()

    # Determine the winner
    if movesDict.get(player1.getLastMove()) == player2.getLastMove():
        print("Player one wins!")
        player1.incrementWinCount()
    elif player1.getLastMove() == player2.getLastMove():
        print("Tie!")
    else:
        print("Player two wins!")
        player2.incrementWinCount()

    # Ask if they want to play again
    resp = input('Play again? (y/n)')
    if resp == 'n' or resp == 'N':
        print(resp)
        playAgain = False

# Display the game statistics
print("Player 1 win count:" + str(player1.getWinCount()))
print("Player 2 win count:" + str(player2.getWinCount()))

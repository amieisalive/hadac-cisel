import random

def init():
    """
    Initialize game
    
    outputs:
        *gameStatus
        * magicNumber
     """
     
    return None, random.randint(1,10)

def processInput():
    """
    Handle player's input
    
    Output:
     * playerNumber: the number entered by the player, or None if the player wants to stop the game
     
    """
    while True:
        word = input("What is the magic number? ")
        if word == "quit":
            return None
        
        try: 
            playerNumber = int(word)
            break
        except ValueError:
            print("pls no word")
            continue
        
        return playerNumber
    
def update(gameStatus, magicNumber, playerNumber):
    """
    Update game state
    
    Inputs:
        * gameStatus: the status of the game
        * magicNumber: the magic number to find
        * playerNumber: the number entered by the player
    Output:
        * gameStatus: the status of the game
        * magicNumber : the magic number to find
    
    """
    
    if playerNumber is None:
        gameStatus = "end"
    elif playerNumber == magicNumber:
        gameStatus = "win"
    elif playerNumber < magicNumber:
        gameStatus = "higher"
    elif playerNumber > magicNumber:
        gameStatus = "lower"
        
    return gameStatus, magicNumber

def render(gameStatus,magicNumber):
    """
    Render game state
    
    Input:
        * gameStatus: the status of the game, "win", "end", "lower" or "higher"
        """
        
    if gameStatus == "win":
        print("you win")
    elif gameStatus == "end":
        print("bye")
    elif gameStatus == "higher":
        print("higher")
    elif gameStatus == "lower":
        print("lower")
    else:
        raise RuntimeError("Unexpected game status {}".format(gameStatus))
        
def runGame():
    gameStatus, magicNumber = init()
    while gameStatus != "win" and gameStatus != "end":
        playerNumber = processInput()
        gameStatus, magicNumber = update(gameStatus,magicNumber,playerNumber)
        render(gameStatus,magicNumber)
        

    input("gg")
        
runGame()
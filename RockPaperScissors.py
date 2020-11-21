import random , sys

wins = 0
losses = 0
ties = 0
while True:
    def getComputerMove():
        number = random.randrange(3)
        movesList = ['Rock', 'Paper', 'Scissors']
        computerMove = movesList[number]
        return computerMove
    computerMove = getComputerMove()
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('(r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()

    if playerMove == 'p':
        playerMove = 'Paper'
        print('Paper Versus..')
    elif playerMove == 'r':
        playerMove = 'Rock'
    elif playerMove == 's':
        playerMove = 'Scissors'
    elif playerMove == 'q':
        break
    else:
        print('Invalid Move please try again!')
        continue
    
    if playerMove == computerMove:
        print('Its A Tie!')
        ties +=1
    elif playerMove == 'Rock' and computerMove == 'Scissors':
        print('You WIN!')
        print('Computer used ('+computerMove+')')
        wins += 1
    elif playerMove == 'Paper' and computerMove == 'Rock':
        print('You WIN!')
        print('Computer used ('+computerMove+')')
        wins += 1
    elif playerMove == 'Scissors' and computerMove == 'Paper':
        print('You WIN!')
        print('Computer used ('+computerMove+')')
        wins += 1
    else:
        print('You Lose..')
        print('Computer used ('+computerMove+')')
        losses +=1
        

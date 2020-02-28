import random
import copy
class ticTacToeGame:
    def __init__(self, turn):

        #map[i][j] i -> row j -> col
        #turn = ture -> computer move
        #player marker = x , comp maker = o
        assert turn in [0,1]
        self.map = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.turn = turn 

    def print(self):
        for i in range (3):    
            print(self.map[i][0], '|' , self.map[i][1] , '|' , self.map[i][2])
            if i < 2:
                print("---------")

    def possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.map[i][j] == ' ':
                    moves.append((i,j))
        return moves

    def move(self, loc):
        assert loc in self.possible_moves()

        if self.turn == 1:
            marker = 'X'
            self.turn = 0
        else:
            marker ='O'
            self.turn = 1

        self.map[loc[0]][loc[1]] = marker

    def get_status(self):
        #0:player won  1:Comp won  2:draw  3:unfinished
        for k in range(3):
            if self.map[k] == ['O','O','O']:
                return 0
            elif self.map[k] ==['X','X','X']:
                return 1
            elif self.map[0][k] == 'O' and self.map[1][k] == 'O' and self.map[2][k] == 'O':
                return 0
            elif self.map[0][k] == 'X' and self.map[1][k] == 'X' and self.map[2][k] == 'X':
                return 1
        
        if self.map[0][0] == 'O' and self.map[1][1] == 'O' and self.map[2][2] == 'O':
                return 0
        elif self.map[0][0] == 'X' and self.map[1][1] == 'X' and self.map[2][2] == 'X':
                return 1
        elif self.map[0][2] == 'O' and self.map[1][1] == 'O' and self.map[2][0] == 'O':
                return 0
        elif self.map[0][2] == 'X' and self.map[1][1] == 'X' and self.map[2][0] == 'X':
                return 1

        if self.possible_moves() == []:
            return 2
        else:
            return 3

def pMCTS(game, simPlayer=False):

    #simPlayer is used to flip win/lose for simulating player

    numPlayouts = 2000
    possible_moves = game.possible_moves()
    results = []
    originalGame = game

    #simulate all possible moves
    for pMove in possible_moves:

        result = {
            'move': pMove,
            'wins': 0,
            'draws': 0,
            'losses': 0
        }

        possibleGame = copy.deepcopy(originalGame)
        possibleGame.move(pMove)

        for i in range(numPlayouts):

            #random game playout
            randomGame = copy.deepcopy(possibleGame)
            while randomGame.get_status() == 3:
                rMoves = randomGame.possible_moves()
                randomGame.move(rMoves[random.randint(0,len(rMoves)-1)])

            #record run 
            status = randomGame.get_status()
            if status == 0:
                if simPlayer:
                    result['wins'] = result['wins'] + 1
                else:
                    result['losses'] = result['losses'] + 1
            if status == 1:
                if simPlayer:
                    result['losses'] = result['losses'] + 1
                else:
                    result['wins'] = result['wins'] + 1
            if status == 2:
                result['draws'] = result['draws'] + 1

        results.append(result)

    #select best move, compute score 
    maxI = 0
    for i in range(len(possible_moves)): 
        a = 1
        b = .999
        c = 0
        results[i]['score'] = (a*results[i]['wins'] + b*results[i]['draws'] + c*results[i]['losses'])/(results[i]['wins'] + results[i]['draws'] + results[i]['losses'])
        if results[i]['score'] > results[maxI]['score']:
            maxI = i

    return results[maxI]['move']







def getUserLoc(game):

    validInput = False

    while not validInput:
        userInput = input().split()
        if len(userInput) != 2:
            print("Invalid format")
        else:
            x,y = map(int, userInput)
            if (x,y) in game.possible_moves():
                validInput = True
            else:
                print( "Invalid move")

    return (x,y)

def play_a_new_game():

    #turn= 1 -> computer move
    turn = random.randint(0,1)
    if turn == 1:
        print("Randmoly choosen: computer will go first")
    else:
        print("Randmoly choosen: human will go first")
    
    print("Coordinates: top left is x = 0 y = 0, bottom right is x = 2 y =2")

    game = ticTacToeGame(turn)
    while game.get_status() == 3:

        if turn == 1:
            #computer turn 
            print("Computer turn.")
            move = pMCTS(game, False)
            game.move(move)
            game.print()
            turn = 0
        else:
            #player turn 
            print("Player turn. Enter location as x y")
            move = getUserLoc(game)
            #move = pMCTS(game, True)   # for pMCTS vs pMCTS
            game.move(move)
            game.print()
            turn = 1
  
    status = game.get_status()
    if status == 0:
        print("player wins")
    if status == 1:
        print("Comptuer wins")
    if status == 2:
        print("Draw")

    return status

if __name__ == '__main__':
    play_a_new_game()

    


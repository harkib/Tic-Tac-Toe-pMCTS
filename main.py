import random

#class repersents tic-tac-toe game
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
            marker = 'O'
            self.turn = 0
        else:
            marker ='X'
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

    return x,y


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
            x,y = getUserLoc(game)
            game.move((x,y))
            game.print()
            turn = 0
        else:
            #player turn 
            print("Player turn. Enter location as x y")
            x,y = getUserLoc(game)
            game.move((x,y))
            game.print()
            turn = 1
        
    print(game.get_status())

if __name__ == '__main__':
  play_a_new_game()


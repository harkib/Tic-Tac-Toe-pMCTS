
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



x = ticTacToeGame(1)

x.move((0,0))
x.print()
print (x.possible_moves())
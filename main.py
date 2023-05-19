class Board():
        #constructor
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]
        #printing current state of the board 
    def display(self):
        print("---------")
        for I in self.board:
            print("|", end=" ")
            for element in I:
                print(element, end=" ")
            print("|")
        print("---------")
        #incializing starting board(for testing only)
    def get_starting_board(self):
        u = list(input("> "))
        for i in range(3):
            for j in range(3):
                self.board[i][j] = u.pop(0)
        return  self.board
        #input from user and checking if it is valid, as argument method takes 'O' or 'X'
    def move(self, x_or_o):
        while True:
            move = input('> ')
            i = move[0]
            j = move[2]
            if not i.isdigit() or not j.isdigit():
                print('You should enter numbers!')
                continue
            i = int(move[0])
            j = int(move[2])
            if i > 3 or i < 1 or j > 3 or j < 1:
                print('Coordinates should be from 1 to 3!')
                continue

            if self.board[i-1][j-1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            break
        self.board[i-1][j-1] = x_or_o
            #method checks if game is over
    def is_over(self):
            # checking for win in level
        for i in range(len(self.board)): 
            if self.board[i][0] != ' ' and all(self.board[i][0] == self.board[i][j] for j in range(1, len(self.board))):
                print(f'{self.board[i][0]} wins!')
                return True
            # checking for win vertically
        for i in range(len(self.board)):
            if self.board[0][i] != ' ' and  all(self.board[0][i] == self.board[j][i] for j in range(1, len(self.board))):
                print(f'{self.board[0][i]} wins!')
                return True
            #checking for win in first diagonal
        if self.board[0][0] != ' ' and all(self.board[0][0] == self.board[i][i] for i in range(1, len(self.board))):
            print(f'{self.board[0][0]} wins!')
            return  True
            #checking for win in second diagonal
        if self.board[0][len(self.board) - 1] != ' ' and all(self.board[0][len(self.board) - 1] == self.board[i][len(self.board) - 1 - i] for i in range(1, len(self.board))):
            print(f'{self.board[0][len(self.board) - 1]} wins!')
            return True
            #checking if board has any free pleaces
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ' ':
                    return False
        print("It's a draw")
        return True
def main():
    play_board = Board()
    play_board.display()
    while True:
        play_board.move('X')
        play_board.display()
        if play_board.is_over() == True:
            break
        play_board.move('O')
        play_board.display()
        if play_board.is_over() == True:
            break

if __name__ == '__main__':
    main()



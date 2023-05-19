class Board():
    def __init__(self):
        self.tablica = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]

    def display(self):
        print("---------")
        for wiersz in self.tablica:
            print("|", end=" ")
            for element in wiersz:
                print(element, end=" ")
            print("|")
        print("---------")

    def get_starting_board(self):
        u = list(input("> "))
        for i in range(3):
            for j in range(3):
                self.tablica[i][j] = u.pop(0)
        return  self.tablica

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

            if self.tablica[i-1][j-1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            break
        self.tablica[i-1][j-1] = x_or_o

    def is_over(self):
        for i in range(len(self.tablica)):
            if self.tablica[i][0] != ' ' and all(self.tablica[i][0] == self.tablica[i][j] for j in range(1, len(self.tablica))):
                print(f'{self.tablica[i][0]} wins!')
                return True

        for i in range(len(self.tablica)):
            if self.tablica[0][i] != ' ' and  all(self.tablica[0][i] == self.tablica[j][i] for j in range(1, len(self.tablica))):
                print(f'{self.tablica[0][i]} wins!')
                return True

        if self.tablica[0][0] != ' ' and all(self.tablica[0][0] == self.tablica[i][i] for i in range(1, len(self.tablica))):
            print(f'{self.tablica[0][0]} wins!')
            return  True

        if self.tablica[0][len(self.tablica) - 1] != ' ' and all(self.tablica[0][len(self.tablica) - 1] == self.tablica[i][len(self.tablica) - 1 - i] for i in range(1, len(self.tablica))):
            print(f'{self.tablica[0][len(self.tablica) - 1]} wins!')
            return True

        for i in range(len(self.tablica)):
            for j in range(len(self.tablica)):
                if self.tablica[i][j] == ' ':
                    return False
        print("It's a draw")
        return True

board = Board()
board.display()
while True:
    board.move('X')
    board.display()
    if board.is_over() == True:
        break
    board.move('O')
    board.display()
    if board.is_over() == True:
        break



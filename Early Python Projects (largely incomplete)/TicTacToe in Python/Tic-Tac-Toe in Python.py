class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print(' ')
        print('-' * 5)
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print(' ')

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    
    def check_win_draw(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return None

        return 'DRAW'

    def switch_player(self, player):
        return 'O' if player == 'X' else 'X'

    def get_legal_moves(self):
        legal_moves = []
        for row in range (3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    legal_moves.append((row, col))
        return legal_moves
        
    def evaluate(self):
        result = self.check_win_draw()
        if result == 'X':
            return 1
        elif result == 'O':
            return -1
        else:
            return 0 # DRaw or non-terminal position
        
    def minimax(self, depth, is_maximizing_player):
        score = self.evaluate()

        if score == 1 or score == -1 or depth == 0 or not self.get_legal_moves():
            return score
        
        if is_maximizing_player:
            best_score = -float('inf')
            for move in self.get_legal_moves():
                row, col = move
                self.board[row][col] = 'X'
                best_score = max(best_score, self.minimax(depth - 1, not is_maximizing_player))
                self.board[row][col] = ' '  # Revert the move
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_legal_moves():
                row, col = move
                self.board[row][col] = 'O'
                best_score = min(best_score, self.minimax(depth - 1, not is_maximizing_player))
                self.board[row][col] = ' ' 
            return best_score

    def find_best_move(self):
        best_move = None
        best_score = -float('inf')

        for move in self.get_legal_moves():
            row, col = move
            self.board[row][col] = 'X'
            move_score = self.minimax(0, False)  # Depth 0 because we already made a move
            self.board[row][col] = ' '  # Revert the move

            if move_score > best_score:
                best_move = move
                best_score = move_score

        return best_move

def get_move():
    row, col = map(int, input("Enter your move (row col): ").split())
    return row - 1, col - 1

def main():
    game = TicTacToe()
    current_player = 'X'

    while True:
        game.display()

        if current_player == 'O':
            row, col = game.find_best_move()
            game.make_move(row, col, current_player)
        else: 
            row, col = get_move()
            if not game.make_move(row, col, current_player):
                print("Invalid move, try again.")
                continue

        result = game.check_win_draw()
        if result:
            game.display()
            if result == 'DRAW':
                print("It's a draw!")
            else:
                print(f"Player {current_player} wins!")
            break

        current_player = game.switch_player(current_player)

if __name__ == "__main__":
    main()
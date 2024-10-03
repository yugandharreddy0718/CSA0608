def game_of_life(board):
    def count_live_neighbors(board, i, j):
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0) and 0 <= i + x < len(board) and 0 <= j + y < len(board[0]):
                    count += board[i + x][j + y] & 1  # Correctly referencing 'board'
        return count

    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = count_live_neighbors(board, i, j)
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 2
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = -1

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 1 if board[i][j] > 0 else 0  

    return board

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
next_state = game_of_life(board)
print(next_state)

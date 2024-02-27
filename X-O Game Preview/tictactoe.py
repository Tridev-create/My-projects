import random

EMPTY = None
X = 'X'
O = 'O'
P = True

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY,  EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns the player who has the next turn on a board.
    """
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)
    
    if count_O == count_X:
        return O
    elif count_X > count_O:
        return O
    elif count_X < count_O:
        return X



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    result = []
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 'EMPTY':
            result.append(board[0][col])

    # เช็ค row
    for i in board:
        if i.count(O) == 3:
            result.append(O)
        elif i.count(X) == 3:
            result.append(X)

    # เช็คมุมทแยง    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        result.append(board[0][0])
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        result.append(board[0][2])
    
    if len(result) >= 1:
        return str(result[0])
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = []
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            result.append(True)
            
    # เช็ค row
    for i in board:
        #print(i.count(O))
        if i.count(O) == 3:
            result.append(True)
        if i.count(X) == 3:
            result.append(True)

        
    # เช็คมุมทแยง    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        result.append(True)
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        result.append(True)

    s = []
    for i in board:
        s.extend(i)


    if len(result) >= 1:
        return str(result)
    elif None not in s:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = []
        # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 'EMPTY':
            result.append(board[0][col])
            
    # เช็ค row
    for i in board:
        if i.count(O) == 3:
            result.append(O)
        if i.count(X) == 3:
            result.append(X)
        
    # เช็คมุมทแยง    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        result.append(board[0][0])
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        result.append(board[0][2])
    #print(result)
    
    if X in result:
        return 1
    elif O in result:
        return -1
    elif EMPTY not in board:
        return 0
    

def action(board):
    column = len(board)

    for i in board:
        row = len(i)

    position = set()

    for i in range(column):
        for j in range(row):
            if board[i][j] == None:
                position.add((i, j))
    
    position = sorted(position)
    print(position)
                
    return position    

    #rint(position)
def minimax(board):
    
    column = len(board)
    for i in board:
        row = len(i)

    position = set()
    block_eniemies = set()

    for i in range(column):
        for row in range(len(board)):
            if board[i].count(O) == 2 and board[i][row] == EMPTY or board[i].count(X) == 2 and board[i][row] == EMPTY:
                block_eniemies.add((i, row))


    for col in range(3):
        for row in range(len(board)):
            data = []
            data.append((board[0][col], board[1][col], board[2][col]))
            if data[0].count(O) == 2 and board[row][col] == EMPTY or data[0].count(X) == 2 and board[row][col] == EMPTY:
                block_eniemies.add((row, col))

    for row in range(len(board)):
        data = []
        data.append((board[0][0], board[1][1], board[2][2]))
        if data[0].count(O) == 2 and board[row][row] == EMPTY or data[0].count(X) == 2 and board[row][row] == EMPTY:
            block_eniemies.add((row, row))
            print('Not O: ', row, row)
    
    
    x = 2
    for row in range(len(board)):
        data = []
        data.append((board[2][0], board[1][1], board[0][2]))
        print(data)
        print(data[0].count('O'))
        if data[0].count(O) == 2 and board[x][row] == EMPTY or data[0].count(X) == 2 and board[x][row] == EMPTY:
            block_eniemies.add((x, row))
        x -= 1

    if len(block_eniemies) >= 1:
        print(block_eniemies)
        move = list(block_eniemies)
        return move[0]#Move
    else:
        datas = []
        Movement = action(board)
        #print(Movement)
        for i in range(column):
                for row in range(len(board)):
                    if (board[i].count(X) <= 2 and board[i][row] == EMPTY):
                        if (board[i].count(X) <= 2 and board[i][row] == EMPTY):
                            print(i, row)
                            datas.append((i, row)) 
                        
        for col in range(3):
                for row in range(len(board)):
                    data = []
                    data.append((board[0][col], board[1][col], board[2][col]))
                    if (data[0].count(X) <= 2 and board[row][col] == EMPTY):
                        if (data[0].count(X) <= 2 and board[row][col] == EMPTY):
                            datas.append((row, col)) 
                            #return (row, col)

        for row in range(len(board)):
                data = []
                data.append((board[0][0], board[1][1], board[2][2]))
                if (data[0].count(X) <= 2 and board[row][row] == EMPTY):
                    if (data[0].count(X) <= 2 and board[row][row] == EMPTY):
                        datas.append((row, row)) 
                        #return (row, row)`
                    

            #print(Movement)
        z = 2
        for row in range(len(board)):
                data = []
                data.append((board[2][0], board[1][1], board[0][2]))
                #print(data)
                #print(data[0].count(O))
                if (data[0].count(X) <= 2 and board[z][row] == EMPTY):
                    if (data[0].count(X) <= 2 and board[z][row] == EMPTY):
                        datas.append((z, row)) 
                        pass
                        #return (z, row)
                z -= 1
        s = []
        for i in board:
            s.extend(i)


        for _ in range(10):
            datas = random.choices(datas)

        #print(s)
        if None in s:
            print(None in data)
            print(datas)
            print('Heloo World')
            return datas[0]
        elif None not in s:
            print('Heyyyy')
            return False


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board is None:
        raise ValueError("Board cannot be None")
    if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        raise ValueError("Board must be a valid 2D list")

    new_board = [row[:] for row in board]  # Create a deep copy of the board
    print(action)
    if type(action) == tuple:
        i, j = action
        #print(i, j)
    elif type(action) == list:
        i, j = action[0]

    latest_value = None
    latest_position = None
    if latest_value != None:
        board.extend(action)

    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    
    print(new_board)

    if count_X > count_O:
        new_board[i][j] = O
        return new_board
    elif count_X < count_O:
        new_board[i][j] = X
        return new_board
    elif count_X == count_O:
        new_board[i][j] = O
        return new_board
    if latest_value == None:
        new_board[i][j] = O
        return new_board

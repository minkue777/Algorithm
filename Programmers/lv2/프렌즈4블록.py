def checkFourBlock(r, c, board):
    if board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1] != '*':
        return True
    else:
        return False

def eraseBlockList(m, n, board):
    BlockList = [(r, c) for r in range(m-1) for c in range(n-1) if checkFourBlock(r, c, board)]
    AllBlockList = []
    for coord in BlockList:
        r, c = coord
        AllBlockList.append((r, c))
        AllBlockList.append((r+1, c))
        AllBlockList.append((r, c+1))
        AllBlockList.append((r+1, c+1))
    return list(set(AllBlockList))

def changeBoard(r, c, s, board):
    block = list(board[r])
    block[c] = s
    block = ''.join(block)
    board[r] = block
    return board

def doEraseBlock(board, eraseList):
    for r, c in eraseList:
        changeBoard(r, c, '*', board)
    return board

def moveBlock(r, c, m, board):
    idx = r+1
    while True:
        if idx == m or board[idx][c] != '*':
            break
        idx += 1
        
    if idx == r+1:
        return board
    
    changeBoard(idx-1, c, board[r][c], board)
    changeBoard(r, c, '*', board)
    return board
    
    
def makeNextBoard(m, n, board):
    for c in range(n):
        for r in range(m-2, -1, -1):
            board = moveBlock(r, c, m, board)
    return board
    
def solution(m, n, board):
    numEraseBlock = 0
    while True:
        print(board)
        eraseList = eraseBlockList(m, n, board)
        if len(eraseList) == 0:
            break
        numEraseBlock += len(eraseList)
        board = makeNextBoard(m ,n, doEraseBlock(board, eraseList))
    return numEraseBlock

board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
print(solution(4, 5, board))
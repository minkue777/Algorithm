def pickDoll(board, line):
    N = len(board)
    if not isinstance(line, int) or not 1 <= line <= N:
        raise ValueError
    
    for idx in range(N):
        pick = 0
        if board[idx][line-1] != 0:
            pick = board[idx][line-1]
            break
            
    board[idx][line-1] = 0
    return board, pick

def checkDollList(dollList):
    N = len(dollList)
    print(dollList, N)
    if N <= 1:
        return False
    
    if dollList[-1] == dollList[-2]:
        del dollList[-2:]
        return True
    return False

def solution(board, moves):
    count = 0
    dollList = []
    for move in moves:
        board, pick = pickDoll(board, move)
        if pick != 0:
            dollList.append(pick)
        if checkDollList(dollList):
            count += 2
    return count

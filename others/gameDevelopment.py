dList = ['N', 'W', 'S', 'E']
direction = {'N': (-1, 0), 'W': (0, -1), 'S': (1, 0), 'E': (0, 1)}
count = 1

def turnLeft(d):
    idx = dList.index(d)
    return dList[(idx+1)%4]

def move(loc, d, front=True):
    dx, dy = direction[d]
    loc[0] += dx * (2*front-1)
    loc[1] += dy * (2*front-1)
    
def checkState(gameMap, loc):
    neighbor = [gameMap[loc[0]+1][loc[1]], gameMap[loc[0]][loc[1]+1], \
                gameMap[loc[0]-1][loc[1]], gameMap[loc[0]][loc[1]-1]]
    for s in neighbor:
        if s == 0: 
            return True
    return False

def oneStep(gameMap, loc, d):
    global count
    move(loc, d)
    if gameMap[loc[0]][loc[1]] == 0:
        gameMap[loc[0]][loc[1]] = 2
        count += 1
    else:
        move(loc, d, front=False)
        
def isSea(gameMap, loc):
    return True if gameMap[loc[0]][loc[1]] == 1 else False

def main(gameMap, loc, d):
    gameMap[loc[0]][loc[1]] = 2
    
    while True:
        if isSea(gameMap, loc):
            break
        printState(gameMap, loc, d)
        if not checkState(gameMap, loc):
            move(loc, d, front=False)
            continue
        d = turnLeft(d)
        oneStep(gameMap, loc, d)

def printState(gameMap, loc, d):
    for r in gameMap:
        print(r)
    print("Present location: {}, Direction: {}, Count: {}".format(loc, d, count))
    
    
gameMap = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
loc = [1, 1]
d = 'N'

main(gameMap, loc, d)



        




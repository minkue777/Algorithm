def show2dList(l):
    for row in l:
        for n in row:
            print(n, end='\t')
        print('\n')
        
def clockwise_rotate_matrix(a):
    row_length = len(a)
    column_length = len(a[0])
    
    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]
    return res

def check(key, lock):
    
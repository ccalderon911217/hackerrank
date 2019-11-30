#

def nextMove(n,r,c,grid):
    (xp,yp) = whereIsP(n,grid)
    (xm,ym) = r,c;
    if ym == yp:
        if xp < xm: #same column, above
            return "UP"
        if xp > xm: #same column, below
            return "DOWN"
    if xm == xp:
        if yp < ym: #same row, left
            return "LEFT"
        if yp > ym: #same row, right
            return "RIGHT"
    if xm < xp:
        if ym < yp:
            return "RIGHT"
        else:
            return "LEFT"
    if ym < yp:
        if xm < xp:
            return "DOWN"
        else:
            return "UP"
    # return ""

def whereIsP(n, grid):
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'p':
                return (x,y)

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

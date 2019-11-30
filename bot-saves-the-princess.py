#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    if grid[0][0] == 'p':
        i = 0
        while i < n-1:
            if i % 2 == 0: 
                print("LEFT")
            else:
                print("UP")
            i = i + 1
        return;
    if grid[0][n-1] == 'p':
        i = 0
        while i < n-1:
            if i % 2 == 0: 
                print("RIGHT")
            else:
                print("UP")
            i = i + 1
        return;
    if grid[n-1][0] == 'p':
        i = 0
        while i < n-1:
            if i % 2 == 0: 
                print("LEFT")
            else:
                print("DOWN")
            i = i + 1
        return;
    if grid[n-1][n-1] == 'p':
        i = 0
        while i < n-1:
            if i % 2 == 0: 
                print("RIGHT")
            else:
                print("DOWN")
            i = i + 1
        return;
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

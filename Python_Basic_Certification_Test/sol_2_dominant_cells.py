import os

def numCells(grid):
    n = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            val = grid[row][col]
            f = 1
            for i in range(max(0, row-1), min(len(grid), row+2)):
                for j in range(max(0, col-1), min(len(grid[0]), col+2)):
                    if (i, j) != (row, col) and val <= grid[i][j]:
                        f = 0
                        break
                if f == 0:
                    break
            else:
                n +=1
    return n

if __name__ == '__main__':

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)
    print(result)
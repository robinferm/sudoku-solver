# grid = [[0,0,3,7,1,8,4,5,0],
#         [4,5,0,0,0,0,7,8,1],
#         [1,8,7,4,0,0,2,0,9],
#         [0,0,0,1,0,0,0,6,7],
#         [7,0,8,2,0,0,0,0,4],
#         [5,0,0,6,8,0,0,2,0],
#         [6,0,2,8,0,0,3,9,5],
#         [0,7,0,0,2,0,0,4,8],
#         [0,0,0,5,6,3,0,0,0]]

grid2 = [['123456789','123456789','3','7','1','8','4','5','123456789'],
        ['4','5','123456789','123456789','123456789','123456789','7','8','1'],
        ['1','8','7','4','123456789','123456789','2','123456789','9'],
        ['123456789','123456789','123456789','1','123456789','123456789','123456789','6','7'],
        ['7','123456789','8','2','123456789','123456789','123456789','123456789','4'],
        ['5','123456789','123456789','6','8','123456789','123456789','2','123456789'],
        ['6','123456789','2','8','123456789','123456789','3','9','5'],
        ['123456789','7','123456789','123456789','2','123456789','123456789','4','8'],
        ['123456789','123456789','123456789','5','6','3','123456789','123456789','123456789']]


def horizontal():
    # For each row in grid
    for row in range(len(grid2)):
        # Create a list of all default nums in puzzle
        nums = []
        for item in grid2[row]:
            if len(item) == 1:
                nums += item

        # For each item in row
        for i in range(len(grid2[row])):
            # If the item is larger than 1
            if len(grid2[row][i]) > 1:
                # Remove impossible nums
                for num in nums:
                    grid2[row][i] = grid2[row][i].replace(num, '')

def vertical():
    for col in range(0, len(grid2[0])):
        nums = []
        for row in grid2:
            if len(row[col]) == 1:
                nums += row[col]

        for i in range(len(grid2)):
            if len(grid2[i][col]) > 1:
                for num in nums:
                    grid2[i][col] = grid2[i][col].replace(num, '')

def square():
    x = 0
    y = 3

    # Get squares
    for _ in range(3):
        nums = []
        # first column
        for i in range(3):
            for j in range(x, y):
                if len(grid2[i][j]) == 1:
                    nums += grid2[i][j]

        for i in range(3):
            for j in range(x, y):
                if len(grid2[i][j]) > 1:
                    for num in nums:
                        grid2[i][j] = grid2[i][j].replace(num, '')
        
        nums = []
        # second column
        for i in range(3, 6):
            for j in range(x, y):
                if len(grid2[i][j]) == 1:
                    nums += grid2[i][j]

        for i in range(3, 6):
            for j in range(x, y):
                if len(grid2[i][j]) > 1:
                    for num in nums:
                        grid2[i][j] = grid2[i][j].replace(num, '')
        
        nums = []
        # third column
        for i in range(6, 9):
            for j in range(x, y):
                if len(grid2[i][j]) == 1:
                    nums += grid2[i][j]
                #print(grid2[i][j])
        #print(nums)

        for i in range(6, 9):
            for j in range(x, y):
                if len(grid2[i][j]) > 1:
                    for num in nums:
                        grid2[i][j] = grid2[i][j].replace(num, '')
        x += 3
        y += 3


def solve():
    print('##### BEFORE ##########')
    for x in grid2:
        print(x)

    for i in range(10):
        horizontal()
        vertical()
        square()

    print('##### AFTER ##########')
    for x in grid2:
        print(x)

solve()
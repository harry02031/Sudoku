


myboard = [
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4],
]


def SolveSudoku(b):
     emptyCoord = find_emptysquare(b)
     if not emptyCoord:
         return True
     else:
         row, column = emptyCoord

     for i in range(1,10):
         if isValid(b, i, (row, column)):
             b[row][column] = i
             if SolveSudoku(b):
                 return True
             else:
                 b[row][column] = 0


     return False





def Printingboard (b):

    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
# b[0] length of each row
        for j in range(len(b[0])):
         if j % 3 == 0 and j != 0:
            print(" | ", end="")
         if j == 8:
            print(b[i][j])
         else:
            print(str(b[i][j])+ " ", end = "")


Printingboard(myboard)

def find_emptysquare(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j) # row, column

    return None


def isValid(b, number, tuple):
    #check row
    for i in range(len(b[0])):
        if b[tuple[0]][i] == number and tuple[1] != i:
            return False

    #check column
    for i in range(len(b)):
        if b[i][tuple[1]] == number and tuple[0] != i:
           return False

    # check 3 by 3 current box
    box_x = tuple[1] // 3
    box_y = tuple[0] // 3
    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if b[row][col] == number and (row,col) != tuple:
                return False

    return True



SolveSudoku(myboard)
print("anslkjrwe")
print("kdslfajsdflk")
Printingboard(myboard)























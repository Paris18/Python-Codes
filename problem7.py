'''Given a 2D array, print it in spiral form. See the following examples.
Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11'''

def listspiralprint(row,col, list):
   strrow = 0
   strcol = 0
   while (strrow < row and strcol < col):
       for i in range(strrow, row) :
           print(list[strrow][i])
       strrow=strrow+1
       for i in range(strrow, col) :
          print(list[i][col-1])
       col=col-1
       if(strrow < row):
           for i in range(col-1, strcol-1, -1) :
               print(list[row - 1][i])
           row= row-1
       if (strcol < col):
           for i in range(row - 1, strrow - 1, -1) :
               print(list[i][strrow-1])
           strcol = strcol + 1

list = [ [1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

row = 4
col=4

listspiralprint(row, col,list)
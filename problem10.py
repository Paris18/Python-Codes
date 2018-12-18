'''Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the given 2D array.

For example, consider the following 2D array.

       10, 20, 30, 40
       15, 25, 35, 45
       24, 29, 37, 48
       32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30'''

'''did using Prism Algorith'''


graph =[[10, 20, 30, 40],
       [15, 25, 35, 45],
       [24, 29, 37, 48],
       [32, 33, 39, 50]]

sorted_array = []
parent_array = [[0,0]]
j = 0
k = int(input("enter Element index: "))

while True:
    j = j+1
    if len(parent_array) < 1:
        break
    mina = parent_array[0]
    minindex = [mina[0],mina[1]]
    mina =  (graph[mina[0]][mina[1]])
    for i in parent_array:
        if mina > (graph[i[0]][i[1]]):
            mina = (graph[i[0]][i[1]])
            minindex = [i[0],i[1]]
    sorted_array.append(minindex)
    parent_array.remove(minindex)
    if(minindex[0] < len(graph) and [minindex[0]+1,minindex[1]] not in parent_array ):
        parent_array.append([minindex[0]+1,minindex[1]])
    if(minindex[1] < len(graph[0]) and [minindex[0],minindex[1]+1] not in parent_array):
        parent_array.append([minindex[0],minindex[1]+1])
    if(j == k):
        print (graph[minindex[0]][minindex[1]])
        break